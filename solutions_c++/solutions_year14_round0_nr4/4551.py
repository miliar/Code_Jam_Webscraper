//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>

using namespace std;

#define mp make_pair
#define rep(i,n) for(int i=0,_n=n;i<_n;i++)
#define reps(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define pi 2.0*acos(0.0)
#define MAX 2147483647
#define MIN -2147483647
#define torad(a) (a*pi)/180.0;
#define eps 0.000000001
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front

typedef long long ll;
typedef vector<int>VI;
typedef map<string,int> MSI;
typedef set<int>SI;
typedef pair<int,int>PAR;
typedef vector<PAR>VP;

ll N, M;
ll memo[(1<<18)][102];
vector<int>number;

ll dp(int bit, int mod, int len) {

    if( len == number.size() ) {
            //cerr << mod << endl;
        return mod == 0;
    }

    ll &ret = memo[bit][mod];
    if( ret != -1) {
        return ret;
    }

    int mark[11];
    ret = 0;
    memset(mark, 0, sizeof(mark));

    for(int i = 0; i < number.size(); i ++) {
        if(len == 0 && number[i] == 0 )continue;
        if( ! (bit & (1<< i)) && mark[number[i]] == 0 ) {
           mark[number[i]] = 1;
           ret += dp(bit|(1<<i), (mod*10 + number[i])%M, len + 1);
        } else {
        }
    }
    return ret;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, cas = 0;
	cin >> T;
	while( ++cas <= T ) {
        cin >> N;
        vector<double> U, V;
        for(int i = 0; i < N; i++) {
            double x;
            cin >> x;
            U.pb(x);
        }
        for(int i = 0; i < N; i++) {
            double x;
            cin >> x;
            V.pb(x);
        }

        sort(U.begin(), U.end());
        sort(V.begin(), V.end());
        vector<double> X = V;

        int ret1 = 0, ret2 = N;

        for(int i = 0; i < U.size(); i++) {
            for(int j = 0; j < X.size(); j++) {
                if( X[j] > U[i] ) {
                    X[j] = -1;
                    ret2 --;
                    break;
                }
            }
        }

        for(int v_index = 0; v_index < V.size(); v_index++) {
            int to_delete = -1;
            for(int i = 0; i < U.size(); i++) {
                if( U[i] > V[v_index]) {
                    if(to_delete == -1) {
                        to_delete = i;
                    } else if( U[to_delete] > U[i]) {
                        to_delete = i;
                    }
                }
            }
            if(to_delete == -1 ) {
                int mini = 1e9;
                for(int i = 0; i < U.size(); i++) {
                    if(U[i] < 0 )continue;
                    if( U[i] < mini) {
                        mini = U[i];
                        to_delete = i;
                    }
                }
            }

            if( U[to_delete] > V[v_index]) {
                ret1 ++;
            }

            U[to_delete] = -1;
        }
        //if( ret1 < ret2 ) cerr << "ERROR " << endl;
        printf("Case #%d: %d %d\n", cas, ret1, ret2);
	}
    return 0;
}
