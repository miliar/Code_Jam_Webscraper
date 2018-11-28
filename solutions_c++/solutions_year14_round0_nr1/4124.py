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
#define N 100005
int a[4][4], b[4][4];
int main(){
    int t;
    int ans = 0;
    int ind1, ind2;
    file;
    file2;
    cin>>t;
    rep(q, t){
        cin>>ind1; --ind1;
        rep(i, 4) rep(j, 4) cin>>a[i][j];
        cin>>ind2; --ind2;
        rep(i, 4) rep(j, 4) cin>>b[i][j];
        ans = 0;
        int m_ans = -1;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
            if(a[ind1][i] == b[ind2][j]){
                ++ans;
                m_ans = a[ind1][i];
            }
        if(ans > 1) printf("Case #%d: Bad magician!\n", q + 1);
        else if(ans == 0) printf("Case #%d: Volunteer cheated!\n", q + 1);
        else if(ans == 1) printf("Case #%d: %d\n" , q + 1, m_ans);
    }
}
