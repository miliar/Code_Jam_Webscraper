#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
    int t,x,r,c,co=1;
    FILE *fp,*fo;
    fp=fopen("D-small-attempt0.in","r");
    fo=fopen("output.txt","w");
    fscanf(fp,"%d",&t);
    while(t--)
    {
        fscanf(fp,"%d%d%d",&x,&r,&c);
        if((r*c)%x!=0)
        {
            fprintf(fo,"Case #%d: RICHARD\n",co++);
            continue;
        }
        else
        {
            if(x==1)
            {
                fprintf(fo,"Case #%d: GABRIEL\n",co++);
                continue;
            }
            else
            if(x==2)
            {
                fprintf(fo,"Case #%d: GABRIEL\n",co++);
                continue;
            }
            else
            if(x==3)
            {
                if((r==1 && c==3) ||(r==3 && c==1))
                   {
                       fprintf(fo,"Case #%d: RICHARD\n",co++);
                        continue;
                   }
                else
                   {
                                       fprintf(fo,"Case #%d: GABRIEL\n",co++);
                                        continue;

                   }
            }
            else
            if(x==4)
            {
                if((r==3 && c==4) ||(r==4 && c==3) || (r==4 && c==4))
                {
                    fprintf(fo,"Case #%d: GABRIEL\n",co++);
                    continue;

                }
                else
                {
                    fprintf(fo,"Case #%d: RICHARD\n",co++);
                        continue;
                }
            }
        }
    }
    return 0;
}
