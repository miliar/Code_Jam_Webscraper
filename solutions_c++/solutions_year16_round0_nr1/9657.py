#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
int t,m=1;
cin>>t;
while(t--)
{

long long int n,k,f,g=0;
vector<long long int> v(10,0);
long long int p=1;
cin>>n;
while(g==0)
{
    long long int x=p*n;
long long int b=x;
    if(x==0)
    {
        cout<<"Case #"<<m<<":"<<" "<<"INSOMNIA"<<"\n";
    break;
    }
    else{

    while(x>0)
    {
   k= x % 10;
   x/= 10;
v[k]++;
    }
f=0;
for(int i=0;i<10;i++)
{
    if(v[i]>=1)
        f++;
}
if(f==10){
g++;
cout<<"Case #"<<m<<":"<<" "<<b<<"\n";

}

 else p++;
}
}
    m++;
}
return 0;
}
