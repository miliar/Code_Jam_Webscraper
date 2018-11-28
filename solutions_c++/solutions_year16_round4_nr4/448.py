#include<bits/stdc++.h>
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
using namespace std;
int T;
long long N,R,P,S,M;
int lvl[30][10100];
int v[101010], retv[101010], OK;
string ret;
int m[200][200];
string sm[200];
int getb(int x){
    int p = 1;
    int ret = 0;
    for(int i=0;i<=5;++i) {
        if(m[x][i])
            ret += p;
        p *= 2;
    }
    return ret;
}
int RCOST,COST;
int bdin[200];
int luat[20];
vector<int> VK;
int MOK;
void backm(int x) {
    if(MOK == 0) return;
    int ok = 0;
    if(x == VK.size()) {
        return;
    } else {
        int nx = VK[x];
        for(int i=0;i<N;++i) {
            if(m[nx][i]==1 && luat[i]==0) {
                luat[i]=1;
                backm(x+1);
                luat[i]=0;
                ok=1;
            }
        }
        if(ok == 0)
            MOK = 0;
    }
}
int checkVX(vector<int> vx) {
    VK = vx;
    MOK = 1;
    backm(0);
    if(MOK)
        return 0;
    return 1;
    return MOK;
}

void check() {
    vector<int> P;
    for(int i=0;i<N;++i) {
        P.pb(i);
    }
    do{
        if(checkVX(P)) {
            return;
        }
    } while(next_permutation(P.begin(),P.end()));
    //cout << "CORRECT" << endl;

    RCOST = min(RCOST,COST);
}
int cnt=0;
void backx(int x, int y) {
    if(x == N) {
        check();
        return;
    }
    else if(y == N) {
        backx(x+1,0);
    } else {
        backx(x,y+1);
        if(m[x][y]==0) {
            ++COST;
            m[x][y]=1;
            backx(x,y+1);
            m[x][y]=0;
            --COST;
        }
    }
}

int main() {
    freopen("testf.in","r",stdin);
    freopen("testx2.out","w",stdout);
    cin >> T;
    for(int tt=1;tt<=T;++tt) {
        for(int i=0;i<=100;++i) {
            for(int j=0;j<=100;++j) {
                m[i][j]=0;
            }
        }
        cin >> N;
        for(int i=0;i<N;++i) {
            cin >> sm[i];
            for(int j=0;j<N;++j) {
                if(sm[i][j] == '1') {
                    m[i][j]=1;
                } else {
                    m[i][j]=0;
                }
            }
        }
        RCOST = 10100;
        cnt = 0;
        backx(0,0);
        //cout << cnt;
        printf("Case #%d: %d\n",tt, RCOST);
    }
}
