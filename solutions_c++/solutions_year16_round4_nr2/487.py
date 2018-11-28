#include<bits/stdc++.h>
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
using namespace std;
int T;
long long N,K;
double rez = 0;
double best[1010][1010];
double PR[1010];
int luat[1010];
int NR;
vector<vector<int> > vx;
vector<int> v;
int check() {
    best[0][0]=1;
    for(int i=1;i<=K;++i) {
        for(int j=0;j<=N;++j)
            best[i][j]=0;
        //cout<<v[i-1]<<"!";
        double P = PR[v[i-1]];
        for(int j=1;j<=N;++j) {
            best[i][j] += best[i-1][j-1] * P;
        }
        for(int j=0;j<=N;++j) {
            best[i][j] += best[i-1][j] * (1-P);
        }
    }
    if(rez < best[K][K/2]) {
        rez = best[K][K/2];
    }

}
void mmake(int st,int dr) {
    v.clear();
    for(int i=1;i<=st;++i) {
        v.pb(i);
    }
    for(int i=1;i<=dr;++i){
        v.pb(N-i+1);
    }
    check();
}
int main() {
    freopen("test1.in","r",stdin);
    freopen("testfin.out","w",stdout);
    cin >> T;
    for(int tt=1;tt<=T;++tt) {
        cin >> N >> K;
        vx.clear();
        for(int i=1;i<=N;++i) {
            cin >> PR[i];
        }
        rez = 0;
        sort(PR+1,PR+N+1);
        for(int i=0;i<=K;++i) {
            mmake(i,K-i);
        }

        printf("Case #%d: %.10f\n",tt,rez);
    }
}
