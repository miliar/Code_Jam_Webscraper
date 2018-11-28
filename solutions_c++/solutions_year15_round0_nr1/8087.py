#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
    freopen("A-large.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int b,c,sum,i,n,t,ex,j,f;
    char a[1010];
    while(scanf("%d",&t)!=EOF){
        for(j=1;j<=t;j++){
            scanf("%d",&n);
        getchar();
        gets(a);
        sum=0;
        ex=0;
        for(i=0;i<=n;i++){
            if(sum<i){
                int f=i-sum;
                ex+=f;
                sum=i;
            }
            sum+=a[i]-48;
        }
        printf("Case #%d: %d\n",j,ex);
        }
    }
    return 0;
}
