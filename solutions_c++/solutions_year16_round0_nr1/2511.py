#include<iostream>
#include<vector>
using namespace std;

int main(){
  int n;
  cin >> n;
  vector<int> vec(n);
  vector<int> ans(n);
  //input
  for(int i=0;i<n;i++){
    cin >> vec[i];
  }

  //calc
  int cnt=0;
  for(auto it:vec){
    if(it==0){
      ans[cnt]=it;
    }else{
      bool check[10]={};
      long long cur=it;
      while(1){
        long long buf = cur;
        while(buf){
          check[buf%10]=true;
          buf/=10;
        }

        bool flag=true;
        for(int i=0;i<10;i++){
          if(check[i]!=false)continue;
          flag=false;
          break;
        }
        if(flag){
          ans[cnt]=cur;
          break;
        }
        cur+=it;
      }
    }
    cnt++;
  }
  //output
  for(int i=0;i<n;i++){
    cout<<"Case #"<<(i+1)<<": ";
    if(ans[i])
      cout<< ans[i];
    else 
      cout<<"INSOMNIA";
    cout<<endl;
  }

  return 0;
}
