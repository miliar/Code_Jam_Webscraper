#include <stdio.h>
int lv[1001];
char sy[1010];
int main(void)
{
    FILE *in,*out;
    in=fopen("input.txt","r");
    out=fopen("output.txt","w");
    int n,m,i,j,t=0,ch=0;
    fscanf(in,"%d",&n);

    for(i=0;i<n;i++){
        ch=0;
        t=0;
        fscanf(in,"%d %s",&lv[i],sy);

        for(j=0;j<=lv[i];j++){
            t+=sy[j]-'0';
            if(j+1>t){
                ch+=j+1-t;
                t+=j+1-t;

            }
        }
        fprintf(out,"Case #%d: %d\n",i+1,ch);


    }


}
