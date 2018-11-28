#include <bits/stdc++.h>

using namespace std;

int main(){
    int T,n,dc,m,tp;
    bool d[10];
    FILE * f;
    f = fopen("A-small-attempt2.in","r");
    FILE * g;
    g = fopen("a-small.out","w+");
    fscanf(f,"%d",&T);
    for(int a=0;a<T;a++){
        fscanf(f,"%d",&n);
        if(n==0) fprintf(g, "Case #%d: INSOMNIA\n",a+1);
        else{
            memset(d,0,sizeof(d));
            dc=0; m=0;
            while(dc<10){
                m++;
                tp=n*m;
                while(tp>0){
                    if(d[tp%10]==0){
                        d[tp%10]=1; dc++;
                    }
                    tp/=10;
                }
            }
            fprintf(g,"Case #%d: %d\n",a+1,n*m);
        }
    }
    return 0;
}
