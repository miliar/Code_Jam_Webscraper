#include<cstdio>
long long a,b,ans[100],num,ac,T;
int check(long long x){
    int tmp[20];
    int hd,tl;
    hd=-1;
    while (x!=0){
          tmp[++hd]=x%10;
          x/=10;
    }
    tl=hd; hd=0;
    while (hd<tl){
          if (tmp[hd]!=tmp[tl]) return 0;
          ++hd;
          --tl;     
    }
    return 1;
}
int main(){
    num=0;
    for (long long k=1; k<=10000000; k++){
        if (check(k)&&check(k*k)) ans[++num]=k*k;
    }
    scanf("%I64d",&T);
    for (int o=1; o<=T; o++){
        scanf("%I64d%I64d",&a,&b);
        ac=0;
        for (int i=1; i<=num; i++){
            if (ans[i]>=a&&ans[i]<=b) ++ac;    
        }
        printf("Case #%d: %I64d\n",o,ac);
    }
    return 0;    
}
