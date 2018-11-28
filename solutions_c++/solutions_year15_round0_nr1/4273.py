#include<cstdio>
#include<cstring>
int t,n,i,j,nr,na,nc;
char s[100100];
FILE *f,*g;
int main(){
    f=fopen("A.in","r");
    g=fopen("A.out","w");
    fscanf(f,"%d",&t);
    while(t--){
        nc++;
        fscanf(f,"%d%s",&n,s);
        nr=na=0;
        for(i=0;i<=n;i++){
            if(nr+na<i&&s[i]){
                na+=i-(nr+na);
            }
            nr+=s[i]-'0';
        }
        fprintf(g,"Case #%d: %d\n",nc,na);
    }



    fclose(f);
    fclose(g);
    return 0;
}
