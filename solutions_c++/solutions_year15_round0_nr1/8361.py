#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;


int main()
{
    FILE *fr,*fw;
    fr=fopen("input.txt","r");
    fw=fopen("output.txt","w");
    int t,i,j;
    fscanf(fr,"%d",&t);

    for(i=0;i<t;i++)
    {
        int high, stand=0, frnd=0;
        char s[99999];
        fflush(stdin);
        fscanf(fr,"%d",&high);
        fflush(stdin);
        fscanf(fr,"%s",s);


        for(j=0;j<=high;j++)
        {
            if(stand<j)
            {
                while(stand!=j)
                {
                    stand++;
                    frnd++;
                }
            }
            stand=stand+s[j]-48;
        }
        fprintf(fw,"Case #%d: %d\n",i+1,frnd);
    }
    fclose(fr);
    fclose(fw);




    return 0;
}
