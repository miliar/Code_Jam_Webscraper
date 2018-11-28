#include<stdio.h>

int main(){
    FILE * fin = fopen("in.txt","r");
    FILE * fout = fopen("out.txt","w");
    int t;
    fscanf(fin,"%d",&t);
    for(int q=1;q<=t;q++)
    {
        int x;
        char s[1010];
        fscanf(fin,"%d",&x);
        fscanf(fin,"%s",s);
        for(int i=0;i<=x;i++)
            s[i]-='0';
        int c=s[0],ans=0;
        for(int i=1;i<=x;i++)
        {
            while(c<i){
                c++;
                ans++;
            }
            c+=s[i];
        }
        fprintf(fout,"Case #%d: %d\n",q,ans);
    }
    fclose(fin);
    fclose(fout);
}
