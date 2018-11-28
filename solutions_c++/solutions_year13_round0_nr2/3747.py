#include <cstdio>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <queue>
#include <list>
#include <stack>
#include <fstream>
#include <bitset>
#include <iomanip>
using namespace std;
#define INF 0x7ffffff
#define eps 1e-9
#define pi 3.14159265358979626
#define LL long long
#define clr(a,b) memset(a,b,sizeof(a))
#define FOR(i,a,b) for (int i=a;i<=b;i++)
#define exch(a,b) {int t111=a;a=b;b=t111;}
#define sp struct point
#define sl struct line
#define zero(x) (((x)>0?(x):-(x))<eps)
#define read(a) scanf("%d",&a);

#define N 50500
#define M 600

int a[M][M],n,m,b[M][M];
int c[M],d[M];

void cut(int x,int y)
{
    int x1,y1;
    FOR(i,0,n-1)
    {
        x1=x>>i;
        x1%=2;
        if (x1==1)
        FOR(j,1,m) b[i+1][j]=1;
    }
    FOR(i,0,m-1)
    {
        y1=y>>i;
        y1%=2;
        if (y1==1)
        FOR(j,1,n) b[j][i+1]=1;
    }
}

bool check()
{
    FOR(i,1,n)
    FOR(j,1,m)
    if (a[i][j]!=b[i][j]) return false;
    return true;
}

bool pro()
{
//    FOR(i,0,(int)pow(2,n)-1) FOR(j,0,(int)pow(2,m)-1)
//    {
//        FOR(k1,1,n) FOR(k2,1,m) b[k1][k2]=2;
//        cut(i,j);
//        if (check()) return true;
//    }
//    return false;

    FOR(i,1,n)
    {
        c[i]=-100;
        FOR(j,1,m) if (a[i][j]>c[i]) c[i]=a[i][j];
    }
    FOR(i,1,m)
    {
        d[i]=-100;
        FOR(j,1,n) if (a[j][i]>d[i]) d[i]=a[j][i];
    }

    FOR(i,1,n)
    FOR(j,1,m)
    if (a[i][j]<c[i] && a[i][j]<d[j]) return false;
    return true;
}

int main()
{
    //freopen("subset.in","r",stdin);freopen("subset.out","w",stdout);
    //freopen("B-large.in","r",stdin);
    //freopen("blarge.out","w",stdout);
    //freopen("a.txt","r",stdin);

    int T;
    scanf("%d\n",&T);

    FOR(kk,1,T)
    {
        printf("Case #%d: ",kk);
        read(n);
        read(m);
        FOR(i,1,n) FOR(j,1,m) scanf("%d",&a[i][j]);

        if (pro()) puts("YES");
        else puts("NO");
    }

    return 0;
}
