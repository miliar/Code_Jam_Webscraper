#include <iostream>
using namespace std;
int main() {
    int t;
    cin>>t;
    for (int k=1;k<=t;k++){
    int i=0,m,p=1,ar[10],dig,x;
    cin>>m;
        if(m==0)
            cout<<"Case #"<<k<<": INSOMNIA"<<"\n";
        else{
    while(i<10){
        x=p*m;
        int n=x;
 while(n>0){
     dig=n%10;
     n=n/10;
     int count=0;
     for(int j=0;j<i;j++){
         if(ar[j]==dig){
             count++;
         }
     }
     if(count==0){
         ar[i]=dig;
         i++;
     }
 }
     p++;   
    }
        }
    cout<<"Case #"<<k<<": "<<x<<"\n";
    }
    return 0;
}