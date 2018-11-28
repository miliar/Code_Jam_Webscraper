#include<stdio.h>
#include<stdlib.h>

int lawn[101][101];

int main()
{
    freopen("out2.txt","w",stdout);
    freopen("B-small-attempt0.in","r",stdin);
    int t,z,i,j,n,m,tod,isx,isy,maxx[101],maxy[101];
    char calx[101],caly[101];
    scanf ("%d",&z);
    for (t=1;t<=z;t++)
    {
        for (i=0;i<n;i++)calx[i] = 0,maxx[i] = 0;
        for (i=0;i<m;i++)caly[i] = 0,maxy[i] = 0;
        isx = 1;
        isy = 1;
        scanf ("%d %d",&n,&m);
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                scanf ("%d",&lawn[i][j]);
            }
        }
        printf ("Case #%d: ",t);
        for (i=0;i<n;i++)
        {
            calx[i] = 1;
            maxx[i] = lawn[i][0];
            for (j=0;j<m-1;j++)
            {
                if (lawn[i][j] != lawn[i][j+1])calx[i] = 2;
                if (maxx[i] < lawn[i][j+1])maxx[i] = lawn[i][j+1];
            }
        }
        for (j=0;j<m;j++)
        {
            caly[j] = 1;
            maxy[j] = lawn[0][j];
            for (i=0;i<n-1;i++)
            {
                if (lawn[i][j] != lawn[i+1][j])caly[j] = 2;
                if (maxy[j] < lawn[i+1][j])maxy[j] = lawn[i+1][j];
            }
        }
        for (i=0;i<n;i++)
        {
            if (calx[i] == 2)
            {
                for (j=0;j<m;j++)
                {
                    if (lawn[i][j] != maxx[i] && caly[j]!=1)
                    {
                        calx[i] = 0;
                        break;
                    }
                }
                if (calx[i] == 2)calx[i] = 1;

            }
            if (calx[i] == 0)isx = 0;
            //printf ("%d\n",calx[i]);
        }
        for (i=0;i<m;i++)
        {
            if (caly[i] == 2)
            {
                for (j=0;j<n;j++)
                {
                    if (lawn[j][i] != maxy[i] && calx[j]!=1)
                    {
                        caly[i] = 0;
                        break;
                    }
                }
                if (caly[i] == 2)caly[i] = 1;
            }
            if (caly[i] == 0)isy =0 ;
            //printf ("%d\n",caly[i]);
        }
        if (!isy && !isx)printf ("NO\n");
        else printf ("YES\n");
    }
    return 0;
}
