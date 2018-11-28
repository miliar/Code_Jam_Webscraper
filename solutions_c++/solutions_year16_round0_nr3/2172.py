#include <bits/stdc++.h>
#define lim 16
typedef long long ll;
using namespace std;

ll base[20][20];
int num[20];
ll divi[20];

void convert_bin(ll x){
    int i=0;
    while (x>0){
        num[i++]=x%2;
        x/=2;
    }
}
ll convert_base(ll b,int n){
    ll x=0;
    for (ll i=0; i<=n-1; i++){
        x+=(num[i]*base[b][i]);
    }
    return x;
}
ll isPrime(ll x){
    for (ll d=3; d*d<=x; d+=2){
        if (x%d==0)return d;
    }
    return 0;
}
int main()
{
    int t,n,j;
    freopen("C-large.in","r",stdin);
    freopen("C-large_output.out","w",stdout);
    for (ll b=2; b<=10; b++){
        ll a=1;
        for (ll i=0; i<=lim; i++){
            base[b][i]=a;
            a*=b;
        }
    }
    scanf("%d",&t);
    for (int _case=1; _case<=t; _case++){
        scanf("%d %d",&n,&j);
        n=lim;
        ll la=base[2][n-1]+1;
        ll lb=base[2][n]-1;
        printf("Case #%d:\n",_case);
        for (ll sol=la; j>0 && sol<=lb; sol+=2){
            convert_bin(sol);
            ll aux=0;
            fill(divi,divi+15,0);
            for (ll b=2; b<=10; b++){
                ll z= convert_base(b,n);
                /*aux=isPrime(z);
                if (aux==0) break;
                else divi[b]=aux;*/
                if (z%(b+1)==0){
                    aux=b+1;
                    divi[b]=aux;
                }
                else {
                    aux=0; break;
                }
            }
            if (aux>0){
                //printf("%d\n",j);
                printf("1100000000000000");
                for (int i=lim-1; i>=0; i--) printf("%d",num[i]);
                for (int i=2; i<=10; i++)printf(" %lld",divi[i]);
                printf("\n");
                j--;
            }
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
