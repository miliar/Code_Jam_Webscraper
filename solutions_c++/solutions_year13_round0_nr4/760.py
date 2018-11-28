#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
#include<vector>
#include<deque>
#include<map>
#include<time.h>
using namespace std;
#define MAX_N 21//初期状態をbox0が開いてるとみる
vector<int> dp[1<<MAX_N];//その状態になるための最良の開ける順序
//bool possible[1<<MAX_N];
int needKey[MAX_N];//iの箱を開けるのに必要な鍵
int haveKey[201];
vector<int> canOpen[201];
vector<int> inBox[MAX_N];
vector<int> ans;
int T,k,n;
void init(){
  //vectorのクリアもする}
  for(int i=0;i<(1<<MAX_N);i++){
    dp[i].clear();
  }
  for(int i=0;i<201;i++){
    haveKey[i]=0;
    canOpen[i].clear();
  }
  for(int i=0;i<MAX_N;i++){
    needKey[i]=0;
    inBox[i].clear();
  }
}
void printBit(int x){
  for(int i= n;i>=0;i--){
    cout<<( (x >> i)&1 );
  }
  cout<<endl;
}
bool existinVec(vector<int> vec,int value){
  for(int i=0;i<(int)vec.size();i++){
    if(vec[i]==value)return true;
  }
  return false;
}
vector<int> marge(vector<int> a,vector<int> b){
  vector<int> result;
  unsigned int ai=0,bi=0;
  while(!(ai==a.size()&&bi==b.size())){
    if(ai==a.size()){
      for(;bi<b.size();bi++)result.push_back(b[bi]);
    }else if(bi==b.size()){
      for(;ai<a.size();ai++)result.push_back(a[ai]);
    }else{
      if(a[ai]>b[bi]){
        result.push_back(b[bi]);
        bi++;
      }else{
        result.push_back(a[ai]);
        ai++;
      }
    }
  }
  return result;
}
map<int,int> haveKeys(int x){//x is bit number
  map<int,int> have;
  for(int i=1;i<=200;i++)have[i]=0;
  for(int i=0;i<=n;i++){
    //rightest is 0
    if((x>>i)&1){
      if(i!=0)have[needKey[i]]--;
      for(int j=0;j<(int)inBox[i].size();j++){
        have[inBox[i][j]]++;
      }
    }
  }
  return have;
}
void printVec(vector<int> vec){
  for(int i=1;i<(int)vec.size();i++){
    if(i!=0)cout<<" ";
    cout<<vec[i];
  }
  cout<<endl;
}
bool lexsmaller(vector<int> a,vector<int> b){//a<b
  if(a.empty()){
    cout<<"lex Erorr"<<endl;
    system("pause");
    return false;
  }
  if(b.empty()){
    return true;
  }
  for(int i=0;i<(int)min(a.size(),b.size());i++){
    if(a[i]==b[i])continue;
    if(a[i]<b[i]){
      return true;
    }else{
      return false;
    }
  }
  return false;
}
vector<int> vecsmaller(vector<int> a,vector<int> b){
  if(lexsmaller(a,b))return a;
  return b;
}
int bitnum(int x){
  int ans=0;
  for(int i=0;i<=n;i++){
    if((x>>i)&1)ans++;
  }
  return ans;
}
bool hasKey(int x,int keynum){
  int ans=0;
  for(int i=0;i<=n;i++){
    if( !((x>>i) & 1 ))continue;
    for(int j=0;j<(int)inBox[i].size();j++){
      if(inBox[i][j]==keynum)ans++;
    }
    if(needKey[i]==keynum)ans--;
  }
  return ( (ans>0)? true: false);
}
vector<int> dfs(int x){//
  vector<int> result;
  if(!dp[x].empty()){
    //printBit(x);
    //printVec(result);
    return dp[x];
  }
  for(int i=0;i<bitnum(x);i++)result.push_back(25);
  for(int i=1;i<=n;i++){
      int y=x-(1<<i);
      if( ((x>>i)&1) && (hasKey(y,needKey[i])) ){
        vector<int> tempvec=dfs(y);
        tempvec.push_back(i);
        result=vecsmaller(result, tempvec);  
      }  
  }
  dp[x]=result;
  //printBit(x);
  //printVec(result);
  return result;
}

//key->1~200
//box 0  1~20
int main(){
  ofstream ofs( "d_answer.txt" );
  time_t t1,t2;
  t1=time(NULL);
  cin>>T;
  for(int t=0;t<T;t++){
    init();
    cin>>k>>n;
    map<int,int> initKey;
    for(int i=1;i<201;i++)initKey[i]=0;
    for(int i=0;i<k;i++){//key at first
      int temp;
      cin>>temp;
      inBox[0].push_back(temp);
      initKey[temp]++;
    }
    for(int i=1;i<=n;i++){
      int temp,inboxnum;
      cin>>temp;
      needKey[i]=temp;
      canOpen[temp].push_back(i);
      cin>>inboxnum;
      for(int j=0;j<inboxnum;j++){
        cin>>temp;
        inBox[i].push_back(temp);
      }      
    }
    for(int i=1;i<=n;i++){
      if(existinVec(inBox[0] ,needKey[i])){
        dp[(1<<i)].push_back(i);
      }else{
        dp[(1 << i )].push_back(25);
      }
    }
    dp[0].push_back(0);
    dp[1].push_back(0);
    vector<int> v;
    v=dfs((1<<(n+1))-1);//0の箱が開いてる
    ofs<<"Case #"<<t+1<<": ";
    if(existinVec(v,25)||(int)v.size()!=n+1){
      ofs<<"IMPOSSIBLE"<<endl;
    }else{
      for(int i=1;i<(int)v.size();i++){
        if(i!=1)ofs<<" ";
        ofs<<v[i];
      }
      ofs<<endl;
      //printVec(v);
    }
    //vを出力
    t2=time(NULL);
    cout<<"Case"<<t+1<<" "<<t2-t1<<endl;
  }
  
  
}
