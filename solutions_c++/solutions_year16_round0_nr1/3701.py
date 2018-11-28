#include <bits/stdc++.h>
using namespace std;
int main() {
int t;
cin>>t;
int c=1;
while(c<=t)
{        
        int n;
cin>>n;
int flag=0;
int k=n;
int a[10];
memset(a,0,sizeof(a));
int m=0,i=1;
flag=0;

while(1)
{
        while(k>0)
        { if(!a[k%10]) {a[k%10]=1;m++;}
                k/=10;
        }
        if(m==10)
        { flag=1; k=i*n;break;}
        if(n*i==n*(i+1)) break;
        i++;
        k=n*i;
}
cout<<"Case #"<<c<<": ";
if(!flag)
cout<<"INSOMNIA"<<endl;
else cout<<k<<endl;
c++;
}
        return 0;
}