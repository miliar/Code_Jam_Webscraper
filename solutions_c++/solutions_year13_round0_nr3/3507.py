#include <iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;


char s[100][100];
int save[102][102];
int path[102][102];
int prime[100000];
int h,w;
int main()
{
    FILE *f = fopen("C-small-attempt0.in","r");
    FILE *ww = fopen("outC.txt","w");
    int n;
    int z=1;
    int a,b;
    fscanf(f,"%d",&n);
    for(int i=2;i<100000;i++)
    {
        for(int j=2;j*i<100000;j++)prime[i*j]=1;
    }
    while(n--)
    {
        fscanf(f,"%d%d",&a,&b);
        int res = 0;
        //a = (a==1)?2:a;
        for(int i=a;i<=b;i++)
        {

            {
                //int g = 1;
                char ss[100]="";
                sprintf(ss,"%d",i);
                //printf("%s\n",ss);
                bool te = false;
                for(int i=0;i<(strlen(ss)/2);i++)
                {
                    if(ss[i] != ss[strlen(ss)-1-i])te=true;
                }
                double tt = sqrt(i);
                int dd = (int)sqrt(i);
                if(tt - (double)dd != 0)te=true;
                if(!te)
                {
                    sprintf(ss,"%d",dd);
                    for(int i=0;i<(strlen(ss)/2);i++)
                    {
                        if(ss[i] != ss[strlen(ss)-1-i])te=true;
                    }
                //printf("%s\n",ss);
                }

                if(!te){res++;}
            }
        }
        fprintf(ww,"Case #%d: %d\n",z++,res);


    }
getchar();
    return 0;
}
