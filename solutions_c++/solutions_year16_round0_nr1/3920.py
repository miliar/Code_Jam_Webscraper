#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int abs(int a){
    return a>0?a:-a;
}

int num[10];
int main(){
    int n,m,a,T,icas=0;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    while(T--){
        memset(num,0,sizeof(num));
        int sum=0;
        scanf("%d",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",++icas);
            continue;
        }
        int m=n;
        while(sum<10){
            int t=n;
            while(t){
                if(num[t%10]==0){
                    sum++;
                    num[t%10]=1;
                }
                t/=10;
            }
            n+=m;
        }
        printf("Case #%d: %d\n",++icas,n-m);
    }
    return 0;
}
