#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<stack>
#include<queue>
#include<vector>
#include<map>
#include<ctime>
#include<set>
#include<string>
using namespace std;
#define ll long long
long long A, B;
char s[1002];
int a[100]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};
int check(ll x)
{
    int len = 0;
    while(x>0)
    {
        s[len++]=x%10;
        x/=10;
    }
    for(int i = 0; i<(len+1)>>1;i++)
        if(s[i]!=s[len-i-1])
            return 0;
    return 1;
}
int main()
{
    int i,j,k,T;
    freopen("C-large.in","r",stdin);
    freopen("3.txt","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%lld%lld",&A,&B);
        ll st = (ll)(sqrt(A*1.0))-1;
        st = max(st,1LL);
        ll sqr = st*st;
        ll res=0;
        //int a = clock();
        /*int num=0;
        for(ll x = 1LL; x<=10000000;x++)
            if(check(x)&&check(x*x))
            {
                cout<<x<<",";
                num++;
            }
        cout<<num<<endl;
        while(sqr<=B)
        {
            if(sqr>=A)
            {
                if(check(st)&&check(sqr))
                {
                    res++;
                    //cout<<sqr<<endl;
                }
            }
            st++;
            sqr=st*st;
        }*/
        //cout<<clock()-a<<endl;
        for(i=0;i<39;i++)
        {
            if((ll)a[i]*(ll)a[i]>=A&&(ll)a[i]*(ll)a[i]<=B)
                res++;
        }
        printf("Case #%d: %lld\n",cas,res);
    }
    return 0;
}
