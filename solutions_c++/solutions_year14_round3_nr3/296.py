#include <stdio.h>
int count(int n,int m,int k);
int min(int x,int y);
int n4[10]={0,5,8,10,12,14,16};

int main(){
    int t,ri,temp,n,m,k,ans;
    FILE *fp;
    fp=fopen("C_small.out","w");
    scanf("%d",&t);
    for (ri=1;ri<=t;ri++){
        scanf("%d %d %d",&n,&m,&k);
        if (n>m){
           temp=m;
           m=n;
           n=temp;
        }
        ans=count(n,m,k);
        fprintf(fp,"Case #%d: %d\n",ri,k-ans);
    }
    return 0;
}

int count(int n,int m,int k){
    int i;
    if (n==1) return 0;
    if (n==2) return 0;
    if (n==3) return min(m-2,(k-2)/3);
    if (m==4){
       i=0;
       while ((k>=n4[i+1])&&(i<4)) i++;
       return i;
    }
    else {
         i=0;
         while ((k>=n4[i+1])&&(i<6)) i++;  
         return i;
    }
}

int min(int x,int y){
    if (x<y) return x;
    return y;
}
