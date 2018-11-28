#include<bits/stdtr1c++.h>
using namespace std;
int main()
{
    FILE *fr=fopen("D-small-attempt0.in","r");
    FILE *fw=fopen("Output.txt","w");
    int tc,x,r,c;
    fscanf(fr,"%d",&tc);
    int ctr=1;
    while(tc--)
    {
        fprintf(fw,"Case #%d: ",ctr++);
        fscanf(fr,"%d%d%d",&x,&r,&c);
        if((r*c)%x==0)
        {
            if(x==1 || x==2)
              fprintf(fw,"GABRIEL\n");
            else if(x==3)
            {
                if(min(r,c)>1)
                   fprintf(fw,"GABRIEL\n");
                else
                    fprintf(fw,"RICHARD\n");

            }
            else if(x==4)
            {
                if(min(r,c)>2)
                   fprintf(fw,"GABRIEL\n");
                else
                    fprintf(fw,"RICHARD\n");
            }


        }
        else
            fprintf(fw,"RICHARD\n");
    }
    return 0;

}
