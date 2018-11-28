#include <iostream>
#include <string.h>
#include <ctype.h>
using namespace std;

int main(){
  long long int t,p,n,i,j,x,c;
  cin>>t;
  p=t;
  while(t--){
    cin>>n;
    int a[10],b[10]={0};
    j=1;
    while(n!=0){
      c=0;
      x=n*j;
      i=0;
      while(x!=0){
        a[i]=x%10;
        b[a[i]]=1;
        x=x/10;
        i++;
      }
      for(i=0;i<10;i++)
        if(b[i]==1) c++;
      if(c==10){
        cout<<"Case #"<<p-t<<": "<<n*j<<endl;
        break;
      }
      j++;
    }
    if(n==0) cout<<"Case #"<<p-t<<": INSOMNIA"<<endl;
  }
  return 0;
}
