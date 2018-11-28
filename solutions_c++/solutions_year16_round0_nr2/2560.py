#include<iostream>
#include<string>
#include<vector>
using namespace std;
void flip(int i,string &str){
  if(str.length()>=i){
    string sub=str.substr(0,i);
    for(int j=0;j<i;j++){
      str[j]= (sub[i-j-1] =='-' ? '+' : '-');
    }
  }
}
bool check(string &str){
  for(int i=0;i<str.length();i++){
    if(str[i]=='-')return false;
  }
  return true;
}
int main(){
  int n;
  cin >> n;
  vector<string> vec(n);
  vector<int> ans(n);
  //input
  for(int i=0;i<n;i++){
    cin >> vec[i];
  }

  for(int i=0;i<n;i++){
    int cnt=0;
    int end=vec[i].length();
    while(!check(vec[i])){
      while(vec[i][end-1]=='+'&&end>0) end--;
      if(vec[i][0]=='-'){
        flip(end,vec[i]);
      }else{
        int j=0;
        for(j=1;j<vec[i].length();j++){
          if(vec[i][j]=='-')break;
        }
        flip(j,vec[i]);
      }
      cnt++;
    }
    ans[i]=cnt;
  }

  //output
  for(int i=0;i<n;i++){
    cout<<"Case #"<<(i+1)<<": ";
    cout<< ans[i];
    cout<<endl;
  }

  return 0;
}
