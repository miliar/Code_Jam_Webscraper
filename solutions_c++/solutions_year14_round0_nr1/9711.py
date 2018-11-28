#include <algorithm>
#include <bitset>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <cmath>
  
using namespace std;
  
#define rep(a, b, e) for(int a = (int) b; a < (int) e; ++a)
#define clr(a, val) memset(a, val, sizeof(a))
#define debug(a) cerr << #a << ": " << a << endl;
#define debugv(b, t) cerr << #b << ":\n"; rep(countvec, 0, t) { cerr << b[countvec] << '\t'; } cerr << endl;
#define debugm(c, t, u) cerr << #c << ":\n"; rep(countmat, 0, t) { rep(countbb, 0, u) { cerr << c[countmat][countbb] << '\t'; } cerr << endl; }
#define INF 1<<30
#define MOD 1000000007
#define MAXN 100

int conversion(string p){ int num; num=atoi(p.c_str()); return num; }
string toString(int h){ stringstream ss; ss<<h; return ss.str(); }
long long gcd(long long a,long long b) {return (b==0 ? a : gcd(b,a%b));}
long long lcm(long long a,long long b) {return (a*(b/gcd(a,b))); }

int V1[MAXN][MAXN];
int V2[MAXN][MAXN];
vector<int> R;
vector<int> C;

int main() {
    #ifndef ONLINE_JUDGE
        ios::sync_with_stdio(true);
        freopen("D:/Sublime/in.txt","r",stdin);
        freopen("D:/Sublime/out.txt","w",stdout);
        clock_t start = clock();
    #endif

        int n; cin>>n;
        rep(i,0,n){
            R.clear();
            C.clear();
            int a; cin>>a;
            rep(j,0,4){
                rep(k,0,4){
                    int num1; cin>>num1;
                    V1[j][k]=num1;
                }
            }
            rep(j,0,4){
                R.push_back(V1[a-1][j]);
            }
            int b; cin>>b;
            rep(j,0,4){
                rep(k,0,4){
                    int num2; cin>>num2;
                    V2[j][k]=num2;
                }
            }
            rep(j,0,4){
                C.push_back(V2[b-1][j]);
            }
            int cnt=0;
            int A[4];
            rep(j,0,4){
                rep(k,0,4){
                    if(R[j]==C[k]) {
                        A[cnt]=R[j];
                        cnt++;
                        break;
                    }
                }
            }
            if(cnt==1) cout<<"Case #"<<(i+1)<<": "<<A[0]<<endl;
            else if(cnt>1) cout<<"Case #"<<(i+1)<<": "<<"Bad magician!"<<endl;
            else if(cnt==0) cout<<"Case #"<<(i+1)<<": "<<"Volunteer cheated!"<<endl;
        }

           
    #ifndef ONLINE_JUDGE 
        fprintf(stderr, "\ntime=%.3lfsec\n", 0.001 * (clock() - start)); 
    #endif
    return 0;
}