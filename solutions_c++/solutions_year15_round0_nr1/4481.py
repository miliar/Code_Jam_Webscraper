#include<stdio.h>

int main() {
    FILE* fin = fopen("A-large.in","r");
    FILE* fout = fopen("out.txt","w");
    int c=1,t;
    fscanf(fin,"%d",&t);
    while(c<=t) {
        int n;
        char x[1010];
        fscanf(fin,"%d %s",&n,x);
        int ans=0,sum=0;
        for(int i=0;i<=n;i++) {
            if(x[i]-'0'>0 && sum<i) {
                ans+=i-sum;
                sum+=i-sum;
            }
            sum+=x[i]-'0';
        }
        fprintf(fout,"Case #%d: %d\n",c,ans);
        c++;
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
