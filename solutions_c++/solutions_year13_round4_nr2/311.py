#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int n;
long long p;
long long a1,a2;
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int ca,cc=0;
    int i;
    scanf("%d",&ca);
    while (ca--){
        cin>>n>>p;
        long long d=(1LL<<n)-p;
        if (d==0){
            a1=a2=(1LL<<n)-1;
            printf("Case #%d: %lld %lld\n",++cc,a1,a2);
            continue;
        }
        int sum=0;
        for (i=n-1;i>=0;i--){
            sum++;
            if ((d>>i)>0) break;
        }
        a1=(1LL<<sum)-2;
        long long s=0;
        sum=0;
        for (i=n-1;i>=0;i--){
            sum++;
            s=s|(1LL<<i);
            if (s>=d) break;
        }
        a2=(1LL<<n)-(1LL<<sum);
        printf("Case #%d: %lld %lld\n",++cc,a1,a2);
    }
    return 0;
}
