// Example program
#include <iostream>
#include <string>
using namespace std;
int iscomplete(int*a){
    for(int i=0;i<10;i++)
        if(a[i]==0) return 0;
    return 1;
}
int main()
{
  unsigned long long n,t;
  cin>>t;
  for(int j=1;j<=t;j++){
      cin>>n;
      if(n==0) cout<<"Case #"<<j<<": INSOMNIA\n";
      else{
        int a[10]={0};
        unsigned long long i=1;
        while(!iscomplete(a)){
            unsigned long long temp = (n*i);
    
            while(temp){
               // cout<<temp%10;
                a[temp%10]=1;
                temp /=10;
            }
            i++;
        }
        cout<<"Case #"<<j<<": "<<n*(i-1)<<endl;
      }
    }
  
}
