//+++++++++++++++++++++++++++++//
////      Karan Aggarwal         //
////       IIIT-Hyderabad        //
////+++++++++++++++++++++++++++++//
//// Topic: 
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<cassert>
#include<sstream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)
#define mod 1000000007
#define pi(n) printf("%d",n)
#define pll(n) printf("%lld",n)
#define sll(n) scanf("%lld",&n)
#define ss(s) scanf("%s",s)
#define ps(s) printf("%s",s)
#define si(n) scanf("%d",&n)
#define pn printf("\n")
#define pw printf(" ")

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
int a[1000];
int main()
{
    int n,m,i,t,j,k;
    LL x;
    int T;
    si(t);
    T=t;
    while(t--)
    {
        LL c=0;
        LL mn=1000000000000000000;
        sll(x);si(n);
        rep(i,n)
            si(a[i]);
        sort(a,a+n);
        rep(i,n)
        {
            if(a[i]<x)
            {
                mn = min(mn,c + n-i-1);
                x+=a[i];
                continue;
            }
                mn = min(mn,c + n-i);
            c++;
            if(x>1)
            {
                x+=(x-1);
                i--;
            }
        }
        cout<<"Case #"<<T-t<<": "<<mn<<endl;
    }
    return 0;
}

