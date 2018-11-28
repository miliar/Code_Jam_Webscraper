#include <iostream>
//#include <fstream>
#include <stdio.h>
using namespace std;

#ifdef DEBUG
#define fin stdin
#define fout stdout
#endif

int t,o;
int n,m;
int x[101],y[101];
int a[101][101];
bool f;

FILE *fin = fopen("B-large.in","r");
FILE *fout = fopen("B.out","w");

int main()
{
    fscanf(fin,"%d",&t);
    o = 0;
    while (t--)
    {
        o++;
        fscanf(fin,"%d %d",&n,&m);
        memset(x,0,sizeof(x));
        memset(y,0,sizeof(y));
        for (int i=1;i<=n;++i)
        for (int j=1;j<=m;++j)
        {
            fscanf(fin,"%d",&a[i][j]);
            if (a[i][j]>x[i]) x[i] = a[i][j];
            if (a[i][j]>y[j]) y[j] = a[i][j];
        }
        f = true;
        for (int i=1;i<=n;++i)
        if (f)
        for (int j=1;j<=m;++j)
        if (x[i]>a[i][j] && y[j]>a[i][j])
        {
            f = false;
            break;
        }
        fprintf(fout,"Case #%d: ",o);
        if (f) fprintf(fout,"YES\n");
        else fprintf(fout,"NO\n");
    }
    return 0;
}
