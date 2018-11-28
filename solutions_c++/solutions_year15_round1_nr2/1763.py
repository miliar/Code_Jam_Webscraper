#include<stdio.h>

int gcd(int a,int b){
    if(b>a) return gcd(b,a);
    if(a%b==0) return b;
    return gcd(b,a%b);
}

int lcm(int a,int b){
    return a*b/gcd(a,b);
}

int main(){
    FILE * fin = fopen("in.txt","r");
    FILE * fout = fopen("out.txt","w");
    int t;
    fscanf(fin,"%d",&t);
    for(int q=1;q<=t;q++)
    {
        int b,n;
        fscanf(fin,"%d %d",&b,&n);
        int b1[1010];
        int b2[1010];
        int l = 1;
        for(int i=0;i<b;i++){
            fscanf(fin,"%d",&b1[i]);
            l = lcm(l,b1[i]);
            b2[i] = 0;
        }

        int mod = 0;
        for(int i=0;i<b;i++)
            mod+=l/b1[i];
        n%=mod;
        if(n==0) n = mod;

        int ans = 0;
        for(int k=0;k<n;k++){
            int mini = 0;
            for(int i=1;i<b;i++)
                if(b2[i]<b2[mini]) mini = i;
            ans = mini;
            int t = b2[mini];
            for(int i=0;i<b;i++)
                b2[i] -= t;
            b2[mini] = b1[mini];
        }
        fprintf(fout,"Case #%d: %d\n",q,ans+1);
    }
    fclose(fin);
    fclose(fout);
}
