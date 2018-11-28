#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A2.out.txt", "w", stdout);

    int T,cs=1;
    long n,i,j,m;
    scanf("%d",&T);
    while(T--){
        scanf("%ld",&n);
        printf("Case #%d:",cs++);
        if(n==0){
            printf(" INSOMNIA\n");
            continue;
        }
        int a[15];
        for(i=0;i<=9;i++) a[i]=0;

        for(i=1;;i++){
            m = i*n;
            while(m){
                int r = m%10;
                m = m/10;
                a[r]=1;
            }
            int x=0;
            for(j=0;j<=9;j++) if(a[j]) x++;
            if(x==10){
                m=i*n;
                break;
            }
        }
        printf(" %ld\n",m);
    }
    return 0;
}
