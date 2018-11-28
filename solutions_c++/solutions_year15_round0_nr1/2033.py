#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <iomanip>
#include <ctime>
#include <cmath>

#define pb push_back
#define mp make_pair
#define F first
#define S second

using namespace std;

const long long INF = 1000000000000000001ll;
const int INFint = (1<<28);
const int MOD = 1000000007;
const long double EPS = 1e-8;


int main(){
    ios_base::sync_with_stdio(0);
//    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t<= T; t++){
        int n;
        string s;
        cin >> n >> s;
        long long ans = 0;
        long long res = s[0] - '0';
        for(int i = 1; i <n+1; i++){
            int x = s[i] - '0';
            //cout << x << ' ';
            if (res - i < 0){
                ans += abs(res - i);
                res += abs(res - i);
            }
            res+= x;

        }
        //cout << endl;
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}
