#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 1000000005
#define eps 1e-9
#define PI acos(-1.0)
#define K (0.017453292519943295769236907684886l)
#define LL long long

using namespace std;

const int maxn=100005;
const int rule[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};

char s[maxn];

int L[maxn],R[maxn],n,a[maxn],flag[maxn];

int Get(char ch)
{
    if (ch=='1') return 1;
    if (ch=='i') return 2;
    if (ch=='j') return 3;
    return 4;
}

int Calc(int x,int y)
{
    int cnt=0;
    if (x<0) cnt++;
    if (y<0) cnt++;
    int temp=rule[abs(x)-1][abs(y)-1];
    if (temp<0) cnt++;
    temp=abs(temp);
    if (cnt&1) return -temp; else return temp;
}

int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,cas=0,x,l;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d %d",&x,&l);
        scanf("%s",s);
        int len=strlen(s);
        for (int i=0;i<x*l;i++)
        {
            int pos=i%len;
            a[i]=Get(s[pos]);
        }
        //printf("%d\n",-1);
        L[0]=a[0];
        for (int i=0;i<x*l;i++)
            flag[i]=0;
        for (int i=1;i<x*l;i++)
        {
            L[i]=Calc(L[i-1],a[i]);
        }
        //printf("%d\n",-1);
        R[x*l-1]=a[x*l-1];
        if (R[x*l-1]==4) flag[x*l-1]=4;
        //printf("%d\n",-1);
        for (int i=x*l-2;i>=0;i--)
        {
            R[i]=Calc(a[i],R[i+1]);
            if (R[i]==4||flag[i+1]==4) flag[i]=4;
        }
        int tag=0;
        if (x*l>=3)
        {
            for (int i=0;i<=x*l-3;i++)
            {
                if (L[i]==2&&R[i+1]==2&&flag[i+2]==4) tag=1;
                if (tag) break;
            }
        }
        if (tag) printf("Case #%d: YES\n",++cas); else printf("Case #%d: NO\n",++cas);
    }
    return 0;
}

