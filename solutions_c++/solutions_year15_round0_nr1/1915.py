#include<cstdio>
#define N 1000

int n;
char s[N+5];

int main(void){
    int i,j,x,y,z;
    int t;
    FILE *in,*out;

    in=fopen("input.txt","r");
    out=fopen("output.txt","w");

    fscanf(in,"%d",&t);
    for(i=1;i<=t;i++){
        fscanf(in,"%d",&n);
        fscanf(in,"%s",s);

        z=0;
        x=0;
        for(j=1;j<=n;j++) {
            z+=(s[j-1]-'0');
            if(z<j){
                x+=j-z;
                z=j;
            }
        }

        fprintf(out,"Case #%d: %d\n",i,x);
    }

    return 0;

}

