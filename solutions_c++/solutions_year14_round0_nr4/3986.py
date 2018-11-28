#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <set>
#include <memory.h>
#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi 2 * acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second
#define file freopen("input.txt","r",stdin)
#define file2 freopen("output.txt", "w",stdout)
using namespace std;
typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;
#define time nlnlkjnlhkjbk
#define inf 100000000000
#define mod 1000000007
#define N 1005
double a[N];
double b[N];
bool used[N];
int main(){
    file;
    file2;
    int t;
    cin>>t;
    int n;
    int ans1, ans2;
    rep(q, t){
        cin>>n;
        rep(i, n) scanf("%lf",&a[i]);
        rep(i, n) scanf("%lf",&b[i]);
        ans1 = 0; ans2 = 0;
        int current;
        sort(a, a + n);
        sort(b, b + n);
        int  i = 0;
        int ind = 0;
        while(ind < n){
            if(a[ind] > b[i]){
                ++ind; ++i; ++ans1;
            }
            else ++ind;
        }
        C(used);
        for(i = 0; i < n; ++i){
            current = 1;
            for(int j = 0; j < n; ++j)
                if(b[j] > a[i] && !used[j])
            {
                used[j] = true;
                current = 0;
                break;
            }
            ans2+=current;
        }
        printf("Case #%d: %d %d\n", q + 1, ans1 , ans2);
    }
}
