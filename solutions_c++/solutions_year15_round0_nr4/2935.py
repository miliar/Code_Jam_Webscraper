#include<stdio.h>

int main(){
    FILE * fin = fopen("in.txt","r");
    FILE * fout = fopen("out.txt","w");
    int t;
    fscanf(fin,"%d",&t);
    for(int q=1;q<=t;q++)
    {
        int x,r,c;
        fscanf(fin,"%d %d %d",&x,&r,&c);
        if(x==1)
            fprintf(fout,"Case #%d: GABRIEL\n",q);
        else if(x==2&&r*c%2==0)
            fprintf(fout,"Case #%d: GABRIEL\n",q);
        else if(x==3&&(r*c%6==0||r*c%9==0))
            fprintf(fout,"Case #%d: GABRIEL\n",q);
        else if(x==4&&(r*c==12||r*c==16))
            fprintf(fout,"Case #%d: GABRIEL\n",q);
        else fprintf(fout,"Case #%d: RICHARD\n",q);
    }
    fclose(fin);
    fclose(fout);
}
