#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<cstdio>
#define fori(a) for(i=0;i<a;i++)
#define forj(a) for(j=0;j<a;j++)
#define fork(a,b) for(k=a;k<b;k++)
int readint()
{
    int t=0;
    char c;
    c=getchar();
    while(c<'0' || c>'9')
        c=getchar();
    while(c>='0' && c<='9')
    {
        t=(t<<3)+(t<<1)+c-'0';
        c=getchar();
    }
    return t;
}
int main()
{
    int i,j,k,t,n,m,l,flagr,flagc;
    FILE *fp,fp2;
    freopen("B-large.in","r",stdin);
    freopen("OutputBLarge.txt","w",stdout);
    t=readint();
    fori(t)
    {
        n=readint();
        m=readint();
        int arr[n][m];
        forj(n) fork(0,m) arr[j][k]=readint();
        flagr=0;
        flagc=0;
        forj(n)
        {
            fork(0,m)
            {
                flagr=0;
                flagc=0;
                for (l=0;l<n;l++)
                {
                    if (arr[l][k]>arr[j][k])
                    {
                        flagr=1;
                        break;
                    }
                }
                if (flagr==1)
                {
                    for (l=0;l<m;l++)
                    {
                        if (arr[j][l]>arr[j][k])
                        {
                            flagc=1;
                            break;
                        }
                    }
                }
                if (flagc!=0&&flagr!=0) break;
            }if (flagc!=0&&flagr!=0) break;
        }

        if (flagr!=0&flagc!=0) printf("Case #%d: NO\n",i+1);
        else printf("Case #%d: YES\n",i+1);
    }

    return 0;
}
/*for (j=0; j<n; j++)
        {
            fork(0,m)
            {
                flagc=0;
                flagr=0;
                for (l=0; l<n; l++)
                {
                    if (arr[l][k]>arr[j][k])
                    {
                        flagc=1;
                        break;
                    }
                }
                for (l=0; l<m; l++)
                {
                    if (arr[j][l]>arr[j][k])
                    {
                        flagr=1;
                        break;
                    }
                }
            }
            if (flagr!=0&&flagc!=0) break;
        }*/
