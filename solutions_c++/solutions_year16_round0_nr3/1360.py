#include<bits/stdc++.h>
#define ll long long
using namespace std;
int A[33];
ll n, J;

int bc(int base, int prim)
{
    ll nn=0, p=1;
    for(int i=n-1; i>=0; i--)
    {
        nn=nn+p*(A[i])%prim;
        nn%=prim;
        p=p*base%prim;
    }
    if(nn==0)
        return prim;
    else return 0;
}

int main()
{
    freopen("outbig.txt", "w", stdout);
    int t;
    cin>>t;

    cin>>n>>J;
    printf("Case #1:\n");

    ll primes[5]={2, 3, 5, 7, 11};


    memset(A, 0, sizeof A);
    vector<int>ans;
    A[0]=1; A[n-1]=1;
    int num=0;
    ll P=(1<<(n-2));
    for(ll i=0; i<P; i++){
        for(int j=0; j<(n-2); j++){
            A[j+1]=0;
            ll R=(ll)(1<<j);
            if(R & i){
                A[j+1]=1;
            }
        }

        ans.clear();
        int g=1;
        for(int j=2; j<=10; j++){
            int f=0;
            for(int k=0; k<5; k++){
                f=bc(j, primes[k]);
                if(f!=0){
                    ans.push_back(f);
                    break;
                }
            }
            if(f==0){
                g=0;
                break;
            }
        }
        if(g){
            for(int j=0; j<n; j++){
                printf("%d", A[j]);
            }
            printf(" ");
            for(int j=0; j<9; j++){
                printf("%d ", ans[j]);
            }
            printf("\n");
            num++;
            if(num==J)
                break;
        }
    }

    return 0;
}
