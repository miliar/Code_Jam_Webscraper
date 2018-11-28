#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
    FILE *fr=fopen("a.in","r");
    FILE *f=fopen("a.out","w");
    int t;
    fscanf(fr,"%d",&t);
    for (int cas=1;cas<=t;cas++)
    {
        int n,tot=0,ans=0;
        char ch;
        fscanf(fr,"%d%c",&n,&ch);
        for (int i=0;i<=n;i++) 
        {
            fscanf(fr,"%c",&ch);
            if (i-tot>ans) ans=i-tot;
            tot=tot+(ch-'0');
        }
        fprintf(f,"Case #%d: %d\n",cas,ans);
    }
    return 0;
}
