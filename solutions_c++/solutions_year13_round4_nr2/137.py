#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int tt=0,T;
    long long i,j,k,l;
    long long n,m;
freopen("B.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        cin>>n>>m;
        long long tm=m;
        tt++;
        printf("Case #%d: ",tt);
        if(m==(1LL<<n)){
            printf("%I64d %I64d\n",(1LL<<n)-1,(1LL<<n)-1);

        }else{
        i=n;j=0;k=1;
        while(i>0&&m>(1LL<<(i-1))){
            k<<=1;
            j+=k;
            m-=(1LL<<(i-1));
            i--;
        }
        printf("%I64d",j);
        m=tm;
        m=(1LL<<n)-m;
        i=n;j=(1LL<<n)-1;k=1;
        while(i>0&&m>(1LL<<(i-1))){
            k<<=1;
            j-=k;
            m-=(1LL<<(i-1));
            i--;
        }
        printf(" %I64d\n",j-1);
        }
    }
    return 0;
}
