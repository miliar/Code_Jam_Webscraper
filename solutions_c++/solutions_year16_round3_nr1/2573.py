/**************************************************************
    Problem:
    User: youmi
    Language: C++
    Result: Accepted
    Time:
    Memory:
****************************************************************/
//#pragma comment(linker, "/STACK:1024000000,1024000000")
//#include<bits/stdc++.h>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <stack>
#include <set>
#include <sstream>
#include <cmath>
#include <queue>
#include <deque>
#include <string>
#include <vector>
#define zeros(a) memset(a,0,sizeof(a))
#define ones(a) memset(a,-1,sizeof(a))
#define sc(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define scs(a) scanf("%s",a)
#define sclld(a) scanf("%I64d",&a)
#define pt(a) printf("%d\n",a)
#define ptlld(a) printf("%I64d\n",a)
#define rep0(i,n) for(int i=0;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)
#define rep_1(i,n) for(int i=n;i>=1;i--)
#define rep_0(i,n) for(int i=n-1;i>=0;i--)
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define lson (step<<1)
#define rson (lson+1)
#define esp 1e-6
#define oo 0x3fffffff
#define TEST cout<<"*************************"<<endl

using namespace std;
typedef long long ll;

int n;

const int maxn=30+10;
struct peo
{
    char id;
    int num;
    void init(char _id,int _num)
    {
        id=_id,num=_num;
    }
}p,q;
struct cmp
{
    bool operator()(const peo &a,const peo &b)
    {
        return a.num<b.num;
    }
};
priority_queue<peo,vector<peo>,cmp>qu;
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    int T_T;
    scanf("%d",&T_T);
    for(int kase=1;kase<=T_T;kase++)
    {
        int a;
        sc(n);
        while(!qu.empty())
            qu.pop();
        int temp=0;
        rep0(i,n)
        {
            sc(a);
            p.init(i+'A',a);
            qu.push(p);
            temp+=a;
        }
        printf("Case #%d:",kase);
        while(temp)
        {
            p=qu.top();
            qu.pop();
            double now=1.0*p.num/temp;
            if(now-0.5>esp)
                printf("%c",p.id);
            else
                printf(" %c",p.id);
            p.num--;
            temp--;
            if(p.num)
                qu.push(p);
        }
        cout<<endl;
    }
}
