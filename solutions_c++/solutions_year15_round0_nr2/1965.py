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

bool comp(int x, int y){
    return (x > y);
}

int main(){
    ios_base::sync_with_stdio(0);
//    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t<= T; t++){
        int n;
        string s;
        cin >> n;
        vector <long long> a(n);
        for(int i = 0; i < n; i++){
            cin >> a[i];
        }
        long long ans = INFint;

        sort(a.begin(), a.end(), comp);
        long long mx = a[0];
        for(int i = 1; i <= mx; i++){
            long long mn = 0;
            for(int j = 0; j < n; j++){
                if (a[j] <= i){
                    break;
                }
                mn+= ceil(1.00 * a[j] / i) - 1;
            }
            ans = min(ans, mn + i);

        }

        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}
