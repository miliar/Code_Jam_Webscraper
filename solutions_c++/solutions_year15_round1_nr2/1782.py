#include<stdio.h>
long long m[1005],b,n,test;
FILE *in,*out;
long long gcd(long long x,long long y){
    long long temp;
    while(y!=0){
        temp=x%y;
        x=y;
        y=temp;
    }
    return x;
}
int main(){
    in=fopen("input.txt","r");
    out=fopen("output.txt","w");
    long long x,y,t,i,j;
    fscanf(in,"%lld",&test);
    for(t=0;t<test;t++){
        fscanf(in,"%lld %lld",&b,&n);
        fscanf(in,"%lld",&m[0]);
        x=m[0];
        for(i=1;i<b;i++){
            fscanf(in,"%lld",&m[i]);
            x*=m[i]/gcd(m[i],x);
        }
        y=0;
        for(i=0;i<b;i++)    y+=x/m[i];
        n--;
        n%=y;
        x=y=0;
        n++;
        for(i=0;;i++){
            for(j=0;j<b;j++){
                if(i%m[j]==0)   x++;
                if(x==n){
                    x=j+1;
                    y=-1;
                    break;
                }
            }
            if(y==-1)   break;
        }
        fprintf(out,"Case #%lld: %lld\n",t+1,x);
    }
    return 0;
}
