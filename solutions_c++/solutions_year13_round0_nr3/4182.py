#include<stdio.h>
#include<stdlib.h>

long long a[1000000];

bool palin(long long k){
    long long a=k, b=0;
    while(k){
        b=b*10 + k%10;
        k/=10;
    }
    return a==b;
}

int main(){
//    FILE * pread = stdin;
//    FILE * pwrite = stdout;
    FILE * pread = fopen("inC.txt", "r");
    FILE * pwrite = fopen("outC.txt", "w");
    
    long long n, i, len=0;
    //scanf("%lld", &n);
    n=10000001;
    for(i=1;i<n;i++)
        if(palin(i) && palin(i*i))
            a[len++]=i*i;
    
    printf("n: %lld\n", len);
    for(i=0;i<len;i++) printf("%lld\n", a[i]);
    
    long long c, s, e, ans, tcases;
    fscanf(pread, "%lld", &tcases);
    for(c=1;c<=tcases;c++){
        fscanf(pread, "%lld %lld", &s, &e);
        ans = 0;
        for(i=0;i<len;i++)
            if(s<=a[i] && a[i]<=e) ans++;
        fprintf(pwrite,"Case #%lld: %lld\n", c, ans);
    }
    system("pause");
    return 0;
}
