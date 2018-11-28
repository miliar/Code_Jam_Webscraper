#include <bits/stdc++.h>
#define in_T int t;for(scanf("%d",&t);t--;)
#define in_I(a) scanf("%d",&a)
#define in_F(a) scanf("%lf",&a)
#define in_L(a) scanf("%lld",&a)
#define in_S(a) scanf("%s",a)
#define newline printf("\n")
#define BE(a) a.begin(), a.end()

using namespace std;
const int mod = 1000000007;
#define MUL(a, b) ((a*1LL*b)%mod)
#define ADD(a, b) ((a+b)%mod)

int main(){
    int z = 0;
    in_T{
        int K, C, S;
        in_I(K);
        in_I(C);
        in_I(S);

        cout<<"Case #"<<++z<<": ";
        if(S != K)
            cout<<"IMPOSSIBLE"<<endl;
        else{
            for(int i = 0;i<K;i++)
                cout<<i+1<<" ";
            cout<<endl;
        }
    }
}
