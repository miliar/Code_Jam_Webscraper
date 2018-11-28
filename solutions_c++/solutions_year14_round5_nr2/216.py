#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;

const int MAXN = 110, MAXHIT = MAXN*10, MAXH = 205;

int N, n, P, Q;
ll S[2];
ll H[MAXN], G[MAXN];

const ll NINF = 0x8f8f8f8f8f8f8f8fLL;
ll f[MAXN][MAXHIT][MAXH];

void update(ll&a, ll b){
    if ( a < b ) a = b;
}

ll solve(){
    memset(f,0x8f,sizeof(f));
    f[0][0][0] = 0;
    ll ans = 0;
    
    ll count_states = 0;
    for( int i = 0; i < n; i++ ){
        for( int s = 0; s < MAXHIT; s++ ){
            bool has = false;
            for( int h = 0; h < H[i]; h++ ){
                if ( f[i][s][h] > NINF )
                {
                    has = true;

                    count_states += 1;
                    
                    //cout << i << " " << s << " " << h <<  " " << f[i][s][h] << endl;

                    update(ans,f[i][s][h]);
                    
                    ll score;
                    int nh, ni, ns;
                    
                    // hit
                    
                    if ( h + (s+1)*P >= H[i] ){
                        int k = (H[i] - h) / P;
                        if ( (H[i]-h) % P != 0 )
                            k += 1;
                        
                        nh = h + (k)*P;
                        ni = i;
                        ns = max(0,s-k);
                        score = 0;
                        if ( nh < H[ni] ){
                        }else{
                            score = G[ni];
                            ni += 1;
                            nh = 0;
                        }
                        if ( k == s+1 ){
                            nh = nh + Q;
                            if ( nh < H[ni] ){
                            }else{
                                ni += 1;
                                nh = 0;
                            }
                        }
                        //cout << " " << score << endl;
                        //cout << " " << ni << " " << ns << " " << nh << " "  <<endl;
                        update(f[ni][ns][nh],f[i][s][h]+score);
                        update(ans,f[ni][ns][nh]);
                    }

                    // skip
                    nh = h + Q;
                    ni = i;
                    ns = s+1;
                    score = 0;
                    if ( nh < H[ni] ){
                    }else{
                        ni += 1;
                        nh = 0;
                    }
                    //cout << " " << score << endl;
                    //cout << " " << ni << " " << ns << " " << nh << " "  <<endl;
                    update(f[ni][ns][nh],f[i][s][h]+score);
                    update(ans,f[ni][ns][nh]);
                }
            }
            if ( ! has )
                continue;
        }
    }
    
    cerr << "status #: " << count_states << endl;
    return ans;
}

int main(){
    int T; cin >> T;
    for(int C=1;C<=T;C++){
        memset(H,0,sizeof(H));
        memset(G,0,sizeof(G));
        cin >> P >> Q >> N;
        n = N;
        for( int i = 0; i < N; i++ )
            cin >> H[i] >> G[i];
        S[0] = P; S[1] = Q;
        ll ans = solve();
        cout << "Case #" << C << ": " << ans << endl;
    }
    return 0;
}
