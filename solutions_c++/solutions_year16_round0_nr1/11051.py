#include<iostream>
using namespace std;

int main(){
long long int n;
    int t,k=0;
   long long int q=0;
    cin>>t;
    for(int i=0;i<t; i++){
    int n,m,l=0,arr[10];
    cin>>n;
    if(0<=n<=1000000){
    int h=n;
    q++;
    if(n==0){
    cout<<"Case #"<<q<<": "<<"INSOMNIA"<<endl;
    continue;
    }
    else{
    for(int i=0;i<10;i++)
    {
    arr[i]=0;
    }
    
    int p=0;
    while(true)
    {l=0;
    p=p+1;
    
    while(n!=0)
    {
    m=n%10;
    for(int i=0;i<10;i++)
    {
    if(m==i)arr[i]=11;
    }
    n=n/10;
    }
    for(int i=0;i<10;i++)
    {
    if(arr[i]!=11)
    {
    l=1;
    break;
    }
    }
    if (l==1)
    {n=(p+1)*h;
    k=n;
    }
    if(l==0) break;
    }
    cout<<"Case #"<<q<<": "<<k<<endl;
    }
    }
    
    }
    }
    
    
	



