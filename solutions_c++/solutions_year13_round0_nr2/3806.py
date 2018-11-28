#include <iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<algorithm>
using namespace std;


char s[100][100];
int save[102][102];
int path[102][102];
int h,w;
int main()
{
    FILE *f = fopen("B-large.in","r");
    FILE *ww = fopen("outB.txt","w");
    int n;
    int z=1;
    fscanf(f,"%d",&n);

    while(n--)
    {

        bool tes = false;
        fscanf(f,"%d%d",&h,&w);
       // fprintf(ww,"%d %d\n",h,w);
        memset(save,0,sizeof(save));
        for(int i=0;i<h;i++)
        {
            for(int j=0;j<w;j++)
            {

                fscanf(f,"%d",&save[i][j]);
                path[i][j] = 100;
                //printf("%d ",save[i][j]);
            }
            //puts("");
        }
        //memset(path,100,sizeof(path));
        for(int b=100;b>=1;b--)
        {
            bool tt = true;
            for(int i=0;i<h;i++)
            {
                tt = true;
                for(int j=0;j<w;j++)
                {
                    if(save[i][j] > b)tt=false;

                }
                if(tt)for(int j=0;j<w;j++)path[i][j] = b;
            }
            //tt = true;
            for(int i=0;i<w;i++)
            {
                tt = true;
                for(int j=0;j<h;j++)
                {
                    if(save[j][i] > b)tt=false;

                }
                if(tt)for(int j=0;j<h;j++)path[j][i] = b;
            }
        }
            for(int i=0;i<h;i++)
            {
                for(int j=0;j<w;j++)
                {
                    //printf("%d ",path[i][j]);
                    if(save[i][j] != path[i][j])tes=true;
                }
                //puts("");
            }

        if(!tes)fprintf(ww,"Case #%d: YES\n",z++);
        else fprintf(ww,"Case #%d: NO\n",z++);


    }
getchar();
    return 0;
}
