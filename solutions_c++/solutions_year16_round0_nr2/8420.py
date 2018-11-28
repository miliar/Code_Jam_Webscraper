#include <bits/stdc++.h>
using namespace std;
int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    string s;
    cin>>s;
    int len=s.length();
    int arr[len];
    for(int j=0;j<len;j++){
      if(s[j]=='+')
        arr[j]=1;
      else
        arr[j]=0;
      }
    int flag,count=0;
    for(int j=0;j<len;){
      flag=arr[j];
      int k;
      k=j;
      while(k<len&&arr[k]==flag)
        k++;
      j=k;
      count++;
      if(j==len&&flag==1)
        count--;

    }
    cout<<"Case #"<<i+1<<": "<<count<<endl;
  }
}
