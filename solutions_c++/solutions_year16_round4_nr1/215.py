/*********************************************************************\
   |--\        ---       /\        |-----------| -----   /-------|    |
   |   \        |       /  \       |               |    /             |
   |    \       |      /    \      |               |   |              |
   |     \      |     /      \     |               |   |----|         |
   |      \     |    / ------ \    |-------|       |        |-----|   |
   |       \    |   /          \   |               |              |   |
   |        \   |  /            \  |               |              /   |
  ---        -------            ------           ----- |---------/    |
                                                                      |
    codeforces = nfssdq  ||  topcoder = nafis007                      |
    mail = nafis_sadique@yahoo.com || nfssdq@gmail.com                |
    IIT,Jahangirnagar University(41)                                  |
                                                                      |
**********************************************************************/

#include <bits/stdc++.h>
using namespace std;

#define xx         first
#define yy         second
#define pb         push_back
#define mp         make_pair
#define LL         long long
#define inf        INT_MAX/3
#define mod        1000000007ll
#define PI         acos(-1.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     ((A).begin(), (A).end())
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)

//cout << fixed << setprecision(20) << p << endl;

template <class T> inline T bigmod(T p,T e,T M){
    LL ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

string ss[3][13];
int ts[3][2] = { {0, 1}, {1, 2}, {0, 2} };

int main() {
    freopen("a.in", "r", stdin);
    freopen("a1.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    ss[0][0] = "P";
    ss[1][0] = "R";
    ss[2][0] = "S";
    
    for(int i = 1; i <= 12; i++){
		for(int j = 0; j < 3; j++){
			string t1 = ss[ ts[j][0] ][i-1], t2 = ss[ ts[j][1] ][i-1];
			if(t1 > t2) swap(t1, t2);
			ss[j][i] = t1 + t2;
		} 
	}
    
    int T; cin >> T;
    FOR(ts, 1, T+1){
        int N, R, P, S; cin >> N >> R >> P >> S;
        cout << "Case #" << ts << ": ";
        int fl = 0;
        for(int i = 0; i < 3; i++){
			int a = 0, b = 0, c = 0;
			REP(j, ss[i][N].size()){
				if(ss[i][N][j] == 'P') a++;
				else if(ss[i][N][j] == 'R') b++;
				else c++;
			}
			if(a == P && b == R && c == S){
				cout << ss[i][N] << endl;
				fl = 1;
			}
		}
		if(fl == 0) cout << "IMPOSSIBLE" << endl;
    }

}
