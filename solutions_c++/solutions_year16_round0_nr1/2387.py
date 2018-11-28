#include<bits/stdc++.h>
using namespace std;

int main(){
    int T,n;
    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");
    fscanf(in,"%d",&T);
    for(int t=1;t<=T;t++){
        fscanf(in,"%d",&n);
        if(n==0) {
            fprintf(out,"Case #%d: INSOMNIA\n",t);
            continue;
        }
        bool r[10];
        for(int i=0;i<10;i++) r[i]=false;
        int total = 0;
        int b=0;
        while(total<10){
            b+=n;
            int a=b;
            while(a!=0){
                int c=a%10;
                a=a/10;
                if(r[c]==false) total++;
                r[c]=true;
            }
        }
        fprintf(out,"Case #%d: %d\n",t,b);
    }
}
