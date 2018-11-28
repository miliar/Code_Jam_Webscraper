#include <stdio.h>
#include <string.h>

char c[1000001];

int main ()
{
    freopen ("Consonants8.in","r",stdin);
    freopen ("Consonants8.out","w",stdout);
    int t,n,k,i,j,l,ans;
    scanf ("%d",&t);
    for (i=1;i<=t;i++)
        {
            l=0; n=-1; ans=0;
            for (j=0;j<strlen(c);j++)
                c[j] = '\0';
            scanf ("%s",c);
            scanf ("%d",&k);
            for (j=0;j<strlen(c);j++)
                {
                    if (c[j]!='a'&&c[j]!='e'&&c[j]!='i'&&c[j]!='o'&&c[j]!='u')
                        l++;
                    else
                        l=0;
                    if (l>=k)
                        {
                            ans+=(strlen(c)-j);
                            ans+=(j-n-k)*(strlen(c)-j);
                            n = j-k+1;
                        }
                }
            printf ("Case #%d: %d\n",i,ans);
        }
    scanf (" ");
    return 0;
}
