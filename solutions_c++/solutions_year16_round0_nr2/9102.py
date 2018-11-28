#include <stdio.h>
#include <string.h>
using namespace std;
char ck[101];
int cntcnt[101];

int main()
{
    FILE* in=fopen("input.txt","r");
    FILE* out=fopen("output.txt","w");

    int i, n, cnt=0, j, num,k;
    fscanf(in,"%d",&num);
    for(i=0;i<num;i++)
    {
        fscanf(in,"\n");
        fgets(ck,101,in);
        n=strlen(ck);

        for(j=n-1;j>=0;j--)
        {
            if(ck[j]=='-')
            {
                cnt++;
                for(k=0;k<=j;k++)
                {
                    if(ck[k]=='-') ck[k]='+';
                    else ck[k]='-';
                }
            }
        }
        cntcnt[i]=cnt;
        cnt=0;
    }

    for(i=0;i<num;i++)
    fprintf(out,"Case #%d: %d\n",i+1,cntcnt[i]);
    return 0;
}
