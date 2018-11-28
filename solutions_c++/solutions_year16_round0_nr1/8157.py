#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Aout.out","w",stdout);
    int ar[11]={0};
    int tt; scanf("%d",&tt);
    for(int y=1; y<=tt; y++){
        for(int i=0; i<=11; i++) ar[i]=0;
        long int n; scanf("%ld",&n);
        if(n==0) printf("Case #%d: INSOMNIA\n",y);
        else{
            for(int i=1; i<=1000; i++){
                long int x=n*i;
                while(x!=0){
                    ar[x%10]++;
                    x=x/10;
                }
                int cnt=0;
                for(int j=0; j<=9; j++){
                    if(ar[j]>0) cnt++;
                }
                if(cnt==10) {printf("Case #%d: %ld\n",y,n*i); break;}
            }
        }
    }
    return 0;
}
