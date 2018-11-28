#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const double pi = acos(-1.0);
const double eps = 1e-8;
//const ll INF=(_I64_MAX)/2;
//#pragma comment(linker, "/STACK:102400000,102400000")
const int inf = 0x3f3f3f3f;
#define maxx(a) memset(a, 0x3f, sizeof(a))
#define minn(a) memset(a, 0xC0, sizeof(a))
#define zero(a) memset(a, 0, sizeof(a))
#define FILL(a,b) memset(a, b, sizeof(a))
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define srep(i,n) for(i = 1;i <= n;i ++)
#define MP make_pair
#define fi first
#define se second
typedef pair <int, int> PII;
typedef pair <ll , ll > PX ;

const int MAXN = 10000000;
const int PN = 664579;
int minp[MAXN + 1], p[PN];//minp[i],i能被第minp[i] 个素数整除， p[i]，第i+1个素数
int initPrime(int n = MAXN) {
     int N = 0;
   //  cout<<n<<endl;
     memset(minp, -1, sizeof(minp));
     for (int i = 2; i <= n; ++i) {
          if (minp[i] == -1){
              p[N] = i, minp[i] = N++;
          }
          for (int j = 0; j < N && i * p[j] <= n; ++j) {
               minp[i * p[j]] = j;
               if (i % p[j] == 0) break;
          }
     }
     return N;
}


ll n, m;


vector<vector<ll> > ans;
int s[1111];
void fk(int x) {
   // cout<<"@@"<<x<<endl;
    ll a = 0;
    int i,j;

    ll tp = 0;
    while(x) {
        s[a++] = x%2;
        x >>= 1;
     //   cout<<s[a-1]<< ' ';
    }

    for(i = n-1;i >= 0;i --) {
        tp *= 10;
        tp += s[i];
    }
    reverse(s,s+a);

   // cout<<endl;
    vector<ll> tmp;
    tmp.push_back(tp);

    REP(i,2,11) {
     //   cout<<"?"<<i<<endl;
        a = 0;
        rep(j,n) {
            a *= i;
            a += s[j];
      //      cout<<a<<endl;
        }
        bool f = 0;
  //      cout<<"?"<<a<<endl;
        rep(j,664579) {
            if (p[j] >= a) break;
            if (a % p[j] == 0) {
                tmp.push_back(p[j]);
                f = 1;break;
            }
        }
        if (!f) return;
     //   cout<<a<<' '<<minp[a]<<' '<<p[minp[a]]<<endl;
     //   if(p[minp[a]] == a) return;
     //   tmp.push_back(p[minp[a]]);
    }


    for(i=1;i<tmp.size();i++){
        a = 0;
        rep(j,n) {
            a *= (i+1);
            a += s[j];
         //   cout<<a<<endl;
        }
   //     cout<<"#"<<tmp[0]<<' '<<i<<' '<<a<<' '<<tmp[i]<<' '<<a%tmp[i]<<endl;
    }

    ans.push_back(tmp);

}

void work() {
    int i,j;
    cin>>n>>m;
    for(i = (1ll<<(n-1))+1; i <(1ll<<n);i +=2) {
        fk(i);

        if(ans.size() >=m) {
   //         cout<<"ok"<<endl;
            break;
        }
    }
    rep(i,ans.size()) {
        rep(j,ans[i].size()) {
            cout<<ans[i][j];
            if(j+1!=ans[i].size()) cout<<' ';
        }
        cout<<endl;
    }
}

int main() {
#ifdef LOCAL
    freopen( "in.txt", "r" , stdin);
 freopen ("out.txt","w",stdout );
#endif

 int zz = initPrime();
 //cout<<zz<<endl;
//     int i;
//     rep(i,10) {
//         cout<<i<<' '<<minp[i]<<endl;
//     }
//     rep(i,10) {
//         cout<<"@@"<<i<<' '<<p[i]<<endl;
//     }

    int T,cas=1;
    cin>>T;
    while(T--) {
        printf("Case #%d:\n",cas++);
        work();
    }



    return 0;
}



