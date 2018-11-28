#include <string>
#include <vector>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<functional>
//--
#include<list>
#include<deque>
#include<bitset>
#include<set>
#include<map>
#include<cstdio>
#include<cstring>
#include<sstream>
#define X first
#define Y second
#define pb push_back
#define pqPair priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > >
#define all(X) (X).begin(),(X).end()

using namespace std;
typedef __int64 ll;


int main(){
  int i,j,k,N,T,t;
  bool f=0;
  cin>>T;
  for(t=1;t<=T;t++){
    f=0;
    cout<<"Case #"<<t<<": ";
    string tmp,master;
    vector<int> nums[112];
    int re=0;
    cin>>N;
    for(i=0;i<N;i++){
      cin>>tmp;
      tmp+="!";
      for(j=1;j<tmp.size();j++){
        int hoge=1;
        while(tmp[j-1]==tmp[j]){
          tmp.erase(j,1);
          hoge++;
        }
        nums[i].pb(hoge);
     //   cout<<hoge<<",";
      }
     // cout<<endl<<tmp<<endl;
      if(i){
        if(master!=tmp){
          cout<<"Fegla Won"<<endl;
          f=1;
          break;
        }
      }else{
        master=tmp;
      }
    }
    for(j=0;j<nums[0].size();j++){
      int mn=1<<30,temp;
      for(k=0;k<N;k++){
        temp=0;
        for(int s=0;s<N;s++)
          temp+=abs(nums[k][j]-nums[s][j]);
        mn=min(mn,temp);
      }
      re+=mn;
   //   cout<<master[j]<<"("<<re<<")"<<endl;
    }
    if(!f)cout<<re<<endl;
  }
  return 0;
}