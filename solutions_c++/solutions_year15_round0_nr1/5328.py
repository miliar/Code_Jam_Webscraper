#include <cstdio>
#include <cstring>
#include <queue>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <bitset>
#include <map>
#include <complex>
#include <ctime>
#include <numeric>
#include <set>
#include <cassert>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;


int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string S;

    int T, smax;
    cin >> T;
    for(int tt = 1; tt <= T; tt++){
        cin >> smax >> S;
        int taken = 0;
        int prev = 0;

        for(int i = 0; i < S.size(); i++){
            if(S[i] > '0'){
                if(i > taken + prev){
                    taken += i - (taken + prev);
                }
                prev += S[i] - '0';
            }
        }

        cout << "Case #" << tt << ": " << taken << endl;
    }

    return 0;
}
