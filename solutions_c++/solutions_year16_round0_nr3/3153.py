#include<bits/stdc++.h>
using namespace std;
#define ll long long int

ll a[11];

ll pow(ll a, ll b)
{
    if(b==0) return 1;
    ll tmp = pow(a,b/2);
    if(b%2==0) return tmp*tmp;
    else return a*tmp*tmp;
}

int isprime(ll n)
{
    int flag = 0;
    for(ll i=2; i*i<=n; ++i){
        if(n%i==0){
            flag = 1;
            break;
        }
    }
    return flag;
}

int main()
{
    ll t,i,j,n,k;
    scanf("%lld", &t);
    for(ll ii=1; ii<=t; ii++){
        scanf("%lld %lld", &n, &j);
        int fl = 0;
        ll jj=0;
        printf("Case #%lld:\n", ii);
        for(i=0; i<(1<<(n-2)) && jj<j; i++){
                fl=0;
            for(ll p=2; p<=10; p++){
                a[p] = 1 + pow(p,n-1);
            }
            for( k=0; k<n-2; k++){
                ll y = 1<<k;
                if(i&y){
                    for(ll l=2; l<=10; l++){
                        a[l] = a[l] + pow(l,k+1);
                       // cout<<a[l]<<" ";
                    }
                }
            }
            for(ll q=2; q<=10; q++){
                if(!isprime(a[q])){
                    fl = 1;
                    break;
                }
            }
            if(fl==0){
                    jj++;
                printf("%lld ", a[10]);
                for(ll q=2; q<=10; q++){
                    for(ll r=2; r*r<=a[q]; r++){
                        if(a[q]%r==0){
                            printf("%lld ",r);
                            break;
                        }
                    }
                }
                printf("\n");
            }
        }
    }
    return 0;
}
