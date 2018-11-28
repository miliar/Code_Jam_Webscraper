#include <bits/stdc++.h>
using namespace std;

int main(){

  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    int n;
    cin>>n;
    //n=i;
    if(n==0){
      cout<<"Case #"<<i+1<<": INSOMNIA\n";
    }
    else{
      long int temp=n,k=1,tempp;
      int count=0 , a[10];
      memset(a,0,sizeof(a));
      while(count!=10){
        tempp=temp*k;
        while(tempp!=0){
          if(a[tempp%10]==0){
            a[tempp%10]=1;
            count++;
          }
          tempp/=10;
        }
        k++;
      }
      k--;
      cout<<"Case #"<<i+1<<": "<<temp*k<<endl;
    }
  }
}
