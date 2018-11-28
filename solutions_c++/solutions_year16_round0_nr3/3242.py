#include <cstdio>
#include <set>
#include <cmath>
using namespace std;
int n,j;
int poly[1000][35],degrees[1000],top=0;
int cc,which;
int a[35];
set<long long> dict;
int degree(int x[35])
{
    for (int i=32-1;i>=0;--i)
        if (x[i]) return i;
    return 0;
}
void show(int x[35])
{
    printf("\n");
    for (int i=0;i<=degree(x);++i)
        printf("%dx^%d+",x[i],i);
    printf("\n");
}
void load_irreducible_polynomials()
{
    poly[0][0]=poly[0][1]=1;
    poly[1][0]=poly[1][2]=1;
    poly[2][0]=poly[2][1]=poly[2][2]=1;
    poly[3][0]=poly[3][1]=poly[3][3]=1;
    poly[4][0]=poly[4][2]=poly[4][3]=1;
    poly[5][0]=poly[5][4]=1;
    poly[6][0]=poly[6][1]=poly[6][4]=1;
    poly[7][0]=poly[7][1]=poly[7][2]=poly[7][4]=1;
    poly[8][0]=poly[8][3]=poly[8][4]=1;
    poly[9][0]=poly[9][2]=poly[9][3]=poly[9][4]=1;
    poly[10][0]=poly[10][1]=poly[10][2]=poly[10][3]=poly[10][4]=1;
    poly[11][0]=poly[11][2]=poly[11][5]=1;
    poly[12][0]=poly[12][3]=poly[12][5]=1;
    poly[13][0]=poly[13][1]=poly[13][3]=poly[13][5]=1;
    poly[14][0]=poly[14][1]=poly[14][3]=poly[14][4]=poly[14][5]=1;
    poly[15][0]=poly[15][1]=poly[15][6]=1;
    poly[16][0]=poly[16][2]=poly[16][6]=1;
    poly[17][0]=poly[17][1]=poly[17][2]=poly[17][6]=1;
    poly[18][0]=poly[18][3]=poly[18][6]=1;

    poly[19][0]=1,poly[19][1]=-1;
    poly[20][0]=1,poly[20][1]=-1,poly[20][2]=1;
    poly[21][0]=1,poly[21][1]=1,poly[21][2]=-1;
    poly[22][0]=1,poly[22][1]=-1,poly[22][2]=-1;
    poly[23][0]=1,poly[23][1]=-1,poly[23][3]=1;
    top=24;
    for (int i=0;i<top;++i)
        degrees[i]=degree(poly[i]);
}
void check(int x[35])
{
    long long xx=0;
    for (int i=0;i<n;++i)
    {
        if (a[i]<0) return ;
        if (a[i]) xx|=(a[i]<<i);
    }
    if (dict.find(xx)==dict.end())
    {
        dict.insert(xx);
        ++cc;
        for (int i=0;i<n;++i)
            printf("%d",a[i]);
        //show(a);
        for (int radix=2;radix<=10;++radix)
        {
            long long ans=0;
            for (int i=degrees[which];i>=0;--i)
                ans=ans*radix+poly[which][i];
            printf(" %lld",(ans>0)?ans:-ans);
        }
        if (cc<j) printf("\n");
    }
}
void fill_tail(int now)
{
    check(a);
    if (cc>=j) return ;
    for (;now<=n-1-degrees[which] && a[now];++now);
    if (now>n-1-degrees[which]) return ;
    bool flag=true;
    for (int i=now;i<=now+degrees[which];++i)
        if (a[i] && poly[which][i-now])
        {
            flag=false;
            break;
        }
    if (flag)
    {
        for (int i=now;i<=now+degrees[which];++i)
            if (poly[which][i-now]) a[i]=poly[which][i-now];
        if (cc<j) fill_tail(now+1);
        for (int i=now;i<=now+degrees[which];++i)
            if (poly[which][i-now]) a[i]=0;
    }
    else if (cc<j) fill_tail(now+1);
}
void digit(int high)
{
    if (cc>=j) return ;
    for (;high && !a[high];--high);
    if (high==0)
    {
        if (a[0]==1) check(a);
        return ;
    }
    bool flag=true;
    for (int i=0;i<=n-1;++i)
        if (i<=degrees[which] && a[i] || i>degrees[which] && a[i]<0)
        {
            flag=false;
            break;
        }
    if (flag)
    {
        // try to fill in the tail
        for (int i=0;i<=degrees[which];++i)
            a[i]=poly[which][i];
        fill_tail(0);
        for (int i=0;i<=degrees[which];++i)
            a[i]=0;
    }
    int quotient=-a[high];
    for (int i=high;i>=high-degrees[which];--i)
        a[i]+=quotient*poly[which][i-high+degrees[which]];
    if (cc<j) digit(high);
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    load_irreducible_polynomials();
    dict.clear();
    int testcase;
    scanf("%d",&testcase);
    for (int ii=1;ii<=testcase;++ii)
    {
        scanf("%d%d",&n,&j);
        printf("Case #%d:\n",ii);
        cc=0;
        for (which=0;which<top;++which)
        {
            if (n-1-degrees[which]<0) continue;
            for (int i=n-1-degrees[which]-1;i>=0;--i)
                a[i]=0;
            for (int i=n-1;i>=n-1-degrees[which];--i)
                a[i]=poly[which][i-(n-1-degrees[which])];
            digit(n-1-degrees[which]);
            if (cc>=j) break;
        }
        if (ii<testcase) printf("\n");
    }
    return 0;
}
