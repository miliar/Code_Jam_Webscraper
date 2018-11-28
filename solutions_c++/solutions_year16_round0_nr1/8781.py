#include <bits/stdc++.h>
using namespace std;

int main() {


int t;
cin>>t;
long long n,q,l;
for(int k =1;k<=t;k++)
{
    bool arr[10]={},f;
    cin>>n; l=n;
    cout<<"Case #"<<k<<": ";
    if(n==0) {cout<<"INSOMNIA"<<endl; continue;}
   for(int j=1;;j++)
    {
        f=1;
        n=l*j;
        
        q=n;
        while(q)
        {
            arr[q%10]=1;
            q/=10;
        }
        for(int i=0;i<10;i++)if(arr[i]==0) f=0;
        if(f) {cout<<n<<endl; break;} 
    }
}
return 0;
}