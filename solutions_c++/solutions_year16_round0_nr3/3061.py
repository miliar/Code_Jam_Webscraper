#include <cstdio>
#define nmax 505
using namespace std;
FILE *f=fopen("date.in","r");
FILE *g=fopen("date.out","w");
const int p[]={0,0,3,2,5,2,7,2,3,2,7};
int s[nmax];
int c[nmax],r;
int n,m,mn=1,v[nmax];

void generating(int k,int o[])
{
    int i,j;
    if (mn>m)
        return;
    if (k==n) {
        for (i=2;i<=10;i++)
            o[i]=(o[i]*i+1)%p[i];
        for (i=2;i<=10;i++) {
            if (o[i])
                return;
        }
        for (i=1;i<=n;i++)
            fprintf(g,"%d",v[i]);
        fprintf(g," ");
        for (i=2;i<=10;i++)
            fprintf(g,"%d ",p[i]);
        fprintf(g,"\n");
        ++mn;
        return;
    }
    int l[nmax]={0};

    v[k]=0;
    for (i=2;i<=10;i++)
        l[i]=(o[i]*i+v[k])%p[i];
    generating(k+1,l);
    v[k]=1;
    for (i=2;i<=10;i++)
        l[i]=(o[i]*i+v[k])%p[i];
    generating(k+1,l);
    v[k]=0;
}
void solve()
{
    int i,j;
    fscanf(f,"%d %d",&n,&m);
    v[1]=1;v[n]=1;
    fprintf(g,"Case #1:\n");
    for (int i=2;i<=10;i++)
        c[i]=1;
    generating(2,c);
}
int main()
{
    int t;
    for (fscanf(f,"%d",&t);t;t--)
        solve();

    return 0;
}
