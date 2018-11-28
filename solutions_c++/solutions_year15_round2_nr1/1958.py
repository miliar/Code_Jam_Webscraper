#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
#define fill(s,v) memset(s,v,sizeof(s))
#define fs first
#define sf second
#define pb push_back
#define mkp make_pair
int a[1000006];
int mini(int no)
{
    long int temp,i, j,n,position,p[20],digits,a[100];
n=no;
for(i=0;n!=0;i++)n=n/10;
digits=i; i-=1;
n=no;
while(n!=0)
{
a[i--]=n%10;
n=n/10;
}

int f=0;
if(a[digits-1]==0)return no;
for(i=digits-1;i>=0;i--)
{
    f*=10;
    f+=a[i];
}
return f;
}
int main()
{
    freopen("input.in", "r", stdin);
freopen("output.txt", "w", stdout);
    int i,j;
    for(i=1;i<21;i++)
        a[i]=i;
    a[21]=13;
    /*for(i=22;i<31;i++)
        a[i]=a[i-1]+1;
    a[31]=14;
    for(i=32;i<41;i++)
        a[i]=a[i-1]+1;
    for(i=41;i<=100;i++)
    {
        int t=i/10;t*=10;t++;
        if(i==t)
        {
            a[i]=a[i-10]+1;
        }
        else a[i]=a[i-1]+1;
    }a[101]=30;
    for(i=102;i<110;i++)
        a[i]=a[i-1]+1;
    a[110]=31;
    for(i=112;i<120;i++)
        a[i]=a[i-1]+1;
    for(i=120;i<200;i++)
    {
        int t=i/10;t*=10;
        if(i==t)
        {
            a[i]=a[i-10]+1;
        }
        else a[i]=a[i-1]+1;
    }
    a[200]=a[199]+1;*/
    for(i=21;i<1000006;i++)
    {
        int m=mini(i);
        if(m>=i)
            a[i]=a[i-1]+1;
        else
        a[i]=min(a[m]+1,a[i-1]+1);
        //cout<<i<<" "<<m<<" "<<a[i]<<"\n";
    }
    int t,ii=1;
    cin>>t;
    while(t--)
    {
        cin>>i;cout<<"Case #"<<ii<<": "<<a[i]<<"\n";ii++;
    }
}
