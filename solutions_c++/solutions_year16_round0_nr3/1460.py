#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long int llu;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define mem(a, v) memset(a, v, sizeof(a))
#define PI acos(-1)
#define S(a) scanf("%d",&a)
#define SL(a) scanf("%lld",&a)
#define S2(a, b) scanf("%d%d",&a,&b)
#define nl printf("\n")
#define DEB(x) cout<<#x<<" : "<<x<<endl;
const ll mod = 1000000007LL;
const int lmt = 10000005;
int upto = 10000000;

int fac[lmt];
vector<int> v;
ll powr[12][20];
void pre(){
    for(int i = 2; i <= 10; i++){
        powr[i][0] = 1;
    }
    for(ll i = 2; i <= 10; i++){
        for(int j = 1; j <= 17; j++){
            powr[i][j] = powr[i][j - 1]*i;
        }
    }
}

void seive(){
    mem(fac, 0);
    for(int i = 2; i*i <= upto; i++){
        if(fac[i] == 0){
            for(int j = 2*i; j <= upto; j+=i){
                fac[j] = i;
            }
        }
    }
    for(int i = 2; i <= upto; i++){
        if(fac[i] == 0)
            v.push_back(i);
    }
}

ll getfac(ll x){
    for(int i = 0; i < v.size(); i++){
        if((x%v[i] == 0) && (x != v[i]))
            return v[i];
    }
    return 0;
}

int main(){
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    pre();
    seive();
    int t;
    S(t);
    for(int tst = 1; tst <= t; tst++){
        printf("Case #%d:\n",tst);
        int n, j, cnt = 0;
        S2(n, j);
        n/=2;
        ll N = (1LL<<(n-1));
        for(ll i = 1; (i < (1LL<<n)) && (cnt < j); i++){
        	if((i&1) == 0) continue;
        	if((i&(1LL<<(n-1))) == 0) continue;
            vector<int> tmp;
            bool flag = true;
            for(int j = 2; j <= 10; j++){
            	ll num = 0;
                for(int k = 0; k < n; k++){
                    if(i&(1<<k))
                        num += powr[j][k];
                }
                ll x = getfac(num);
                if(x == 0){
                    flag = false;
                    break;
                }
                else
                    tmp.push_back(x);
            }
            if(flag){
                cnt++;
                for(int j = n-1; j >= 0; j--){
                    if(i&(1<<j))
                        printf("1");
                    else
                        printf("0");
                }
                for(int j = n-1; j >= 0; j--){
                    if(i&(1<<j))
                        printf("1");
                    else
                        printf("0");
                }
                for(int j = 0; j < tmp.size(); j++)
                    printf(" %d",tmp[j]);
                nl;
            }
        }
    }
    return 0;
}