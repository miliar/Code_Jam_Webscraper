#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    FILE *fr=fopen("b.in","r");
    FILE *fw=fopen("b.out","w");
    int t; fscanf(fr,"%d",&t);
    for (int cas=1;cas<=t;cas++)
    {
        int n,a[10000];
        fscanf(fr,"%d",&n);
        for (int i=0;i<n;i++) fscanf(fr,"%d",&a[i]);
        int ans=1000;
        for (int i=1;i<ans;i++)
        {
            int tot=i;
            for (int j=0;j<n;j++)
                tot=tot+(a[j]-1)/i;
            if (tot<ans) ans=tot;
        }
        fprintf(fw,"Case #%d: %d\n",cas,ans);
    }
    return 0;
}
