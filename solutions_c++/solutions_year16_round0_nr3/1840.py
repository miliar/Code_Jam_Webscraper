#include <bits/stdc++.h>
using namespace std;
/* macros */
// memory
#define zeroset(A) memset((A), 0, sizeof((A)))
#define negset(A) memset((A), -1, sizeof((A)))
#define all(c) (c).begin(), (c).end()
#define pb push_back
// input & output
#define inpt(a) freopen(a,"r",stdin)
#define otpt(a) freopen(a,"w",stdout)
#define eol "\n"
// types
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<ll,ll> pll;
#define ff first
#define ss second
// constants
#define EPS 1e-9
#define MAXN 300005
#define INF INT_MAX
#define MOD 1000000007

vector<int> primes;

void readPrimes(){
    inpt("primes.txt");
    int x;
    while(scanf("%d", &x) != EOF){
        primes.pb(x);
    }
}

struct JamCoin{
    ll num;
    int div[11];
    int cnt = 0;

    JamCoin(ll msk){
        num = msk;
        zeroset(div);
    }

    void addDiv(int d){
        ll msk = num;
        int tmp[11] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        while(msk){
            for(int b = 2; b<=10; ++b)
                tmp[b] = (tmp[b] * b + (msk&1LL))%d;
            msk >>= 1;
        }
        for(int b = 2; b<=10; ++b){
            if(tmp[b] == 0 && div[b] == 0){
                div[b] = d;
                cnt ++;
            }
        }
    }

    string toString(){
        string ret = "";
        ll msk = num;
        while(msk){
            ret += "0";
            ret.back() += (msk&1LL);
            msk >>= 1;
        }
        cout << ret;
        return ret;
    }

    void print(){
        this->toString();
        for(int i=2; i<=10; ++i){
            cout << " " << div[i];
        }
        cout << eol;
    }
};

int main()
{
    readPrimes();
    ios::sync_with_stdio(false);
    inpt("sample.in");
    //inpt("");
    otpt("c_large.out");
    int T;
    scanf("%d", &T);
    //for(int ts = 1; ts<=T; ++ts){
        int n, j;
        scanf("%d%d", &n, &j);
        ll msk = (1LL << (n-1)) | 1LL;
        vector<JamCoin> ans;
        for(ll i=(1LL<<15); j&&i>=0; --i){
            JamCoin jc(msk | (i << 1));
            for(auto d : primes){
                jc.addDiv(d);
                if(jc.cnt == 9)
                    break;
            }
            if(jc.cnt == 9){
                ans.pb(jc);
                j--;
            }
        }
        cout << "Case #1:\n";
        for(auto j : ans)
            j.print();
    //}
    return 0;
}
