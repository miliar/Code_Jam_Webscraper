#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

FILE *pfile;
FILE *pfile2;
bool nn[10];
bool kk[10];

int main()
{
    pfile = fopen ("myfile.txt","r");
    pfile2= fopen ("myfile2.txt","w");
    int t;
    int p=1;
    fscanf(pfile,"%d",&t);
    while (p<=t)
    {
        int n;
        fscanf(pfile,"%d",&n);
        float ken[n+5],naom[n+5];
        for(int i =0 ; i < n ; i++)
        {
            fscanf(pfile,"%f",&naom[i]);
        }

        for(int i =0 ; i < n ; i++)
        {
            fscanf(pfile,"%f",&ken[i]);
        }
        sort(naom ,naom+n);
        sort(ken, ken +n);
        int points=0,winn=0;
        int c1=0,c2=n-1;
        while (1)
        {
            int i=0;
            int j=c2;
            for(i=n-1;i>=c1;i--)
            {
                if(naom[i]<ken[j])
                {
                    points=0;
                    break;

                }
                else
                    points++;
                j--;
            }
            if(i<c1)
            {
                winn=points;
                break;
            }
            kk[c2]=true;
            nn[c1]=true;
            c1++;
            c2--;
            if(c2<0)
                break;
        }

        points=0;
        int j=n-1;
        for(int i=n-1 ; i>=0;i--)
        {
            if(naom[i]<ken[j])
            {
                points++;
                j--;
            }

        }
        fprintf(pfile2,"Case #%d: %d %d\n",p,winn,n-points);
        p++;
    }
}
