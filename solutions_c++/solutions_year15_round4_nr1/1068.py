#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pi 3.14159265358979323846264338327950288
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SZ(x) ((int)x.size())
#define mid (l + r) / 2
#define Left k * 2, l, mid
#define Right k * 2 + 1, mid + 1, r
#define N 111
using namespace std;

int n, m;
char ma[N][N];
const char directions[] = { '^' , 'v',  '<' , '>' };
const int delta[][2] = { {-1 , 0} , {1 , 0} , {0 , -1} , {0 , 1} };
class solve{
public :
    void Solve(int cas){
    cin >> n >> m;
    for (int i = 0 ; i < n ; ++i)
        cin >> ma[i];

    int ans = 0;

    for (int i = 0 ; i < n ; ++i)
        for (int j = 0 ; j < m ; ++j){
            if (ma[i][j] != '.'){
                bool flag = false;
                int d;

                for (int k = 0 ; k < 4 ; ++k)
                    if (ma[i][j] == directions[k]){
                        d = k;
                        break;
                    }
                int x = i + delta[d][0];
                int y = j + delta[d][1];
                while (x >= 0 && x < n && y >= 0 && y < m){
                    if (ma[x][y] != '.'){
                        flag = true;
                        break;
                    }
                    x += delta[d][0];
                    y += delta[d][1];
                }
                if (!flag){
                    ++ans;
                    for (int k = 0 ; k < 4 ; ++k){
                        int x = i + delta[k][0];
                        int y = j + delta[k][1];
                        while (x >= 0 && x < n && y >= 0 && y < m){
                            if (ma[x][y] != '.'){
                                flag = true;
                                break;
                            }
                            x += delta[k][0];
                            y += delta[k][1];
                        }
                    }
                    if (!flag){
                        cout << "Case #" << cas << ": " << "IMPOSSIBLE" << endl;
                        return ;
                    }
                }
            }
        }

    cout << "Case #" << cas << ": " << ans << endl;
}
}Sol;
int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1 ; i <= t ; ++i)
        Sol.Solve(i);
    return 0;
}
