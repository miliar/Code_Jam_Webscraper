#include<iostream>
#include<cstdio>
#include<climits>
#include<algorithm>
#include<string>
#include<cstring>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<bitset>
#include<cmath>

#define f(i,a,b) for(int i=a;i<b;i++)
#define b(i,a,b) for(int i=a;i>b;i--)
#define mpr(a,b) make_pair(a,b)
#define pr pair<int,int>
#define si(a) scanf("%d",&a)
#define sll(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define newline printf("\n")
#define ll long long 
using namespace std;
int value[11],y=0;
ll op(int s[],ll b)
{
    ll p=1,sum=0;
    b(i,15,-1)
    {
        if(s[i]==1)
            sum+=p;
        p=p*b;
    }
    return sum;
}
bool check(int a[])
{
    int d=0;
    f(m,2,11)
    {
        int c=0;
        ll u=op(a,m);
        f(k,2,100)
        {
            if(u%k==0)
            {   
                value[m]=k;c=1;
            }
            //cout<<c<<" "<<m<<" "<<u<<"   ";
        }
        d+=c;
    }
    if(d==9) {y++;return true;}
    return false;
}
main()
{
    freopen("input1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int a[16]={0},cnt=0;
    int num,clim,test;
    cin>>test;
    cin>>num>>clim;
    cout<<"Case #1:\n";
    f(i,0,16)
    {
        a[i]=1;
        b(j,15,-1)
        {
            if(j-i>1)
            {
                a[j]=1;
                if(check(a)==1&&cnt++<50)
                {
                    f(r,0,16)
                    cout<<a[r];
                    cout<<" ";
                    f(r,2,11)
                    cout<<value[r]<<" ";
                    newline;
                }
            }
        }
        f(k,i+1,16)
        a[k]=0;
    }
    //cout<<y;
}
