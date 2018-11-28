#include <stdio.h>

int a[100][100],qx[2000],qy[2000];
char c[100][100];

int main ()
{
    freopen ("Lawnmower30.in","r",stdin);
    freopen ("Lawnmower30.out","w",stdout);
    int n,i,j,s,l,x,y,max,check;
    scanf ("%d",&n);
    for (i=0;i<n;i++)
        {
            max = -1; check = 0;
            int chx[101]={0},chy[101]={0},hash[101]={0};
            for (j=0;j<100;j++)
                for (l=0;l<100;l++)
                    c[j][l] = ' ';
            scanf ("%d %d",&x,&y);
            for (j=0;j<x;j++)
                for (l=0;l<y;l++)
                    {
                        scanf ("%d",&a[j][l]);
                        hash[a[j][l]] = 1;
                        if (a[j][l]>max)
                            max = a[j][l];
                    }
            for (j=0;j<x;j++)
                for (l=0;l<y;l++)
                    if (a[j][l]==max)
                        {
                            c[j][l] = '*';
                            chx[j] = 1;
                            chy[l] = 1;
                        }
            max--;
            while (hash[max]==0)
                max--;
            while (max>0)
                {
                    s=0;
                    for (j=0;j<x;j++)   
                        if (chx[j]==0)
                            for (l=0;l<y;l++)
                                if (a[j][l]==max)
                                    {
                                        c[j][l] = '*';
                                        qx[s] = j;
                                        qy[s] = l;
                                        s++;
                                    }
                    for (j=0;j<y;j++)   
                        if (chy[j]==0)
                            for (l=0;l<x;l++)
                                if (a[l][j]==max)
                                    {
                                        c[l][j] = '*';
                                        qx[s] = l;
                                        qy[s] = j;
                                        s++;
                                    }
                    for (j=0;j<s;j++)
                        {
                            chx[qx[j]] = 1;
                            chy[qy[j]] = 1;
                            qx[j] = 0;
                            qy[j] = 0;
                        }
                    max--;
                    while (hash[max]==0)
                        max--;
                }
            for (j=0;j<x;j++)
                for (l=0;l<y;l++)
                    if (c[j][l]!='*')
                        check = 1;
            if (check)
                printf ("Case #%d: NO\n",i+1);
            else
                printf ("Case #%d: YES\n",i+1);
        }
    scanf (" ");
    return 0;
}
