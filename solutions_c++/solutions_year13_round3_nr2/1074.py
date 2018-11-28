#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <complex>
using namespace std;
 
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<int> pnt;
typedef pair<int, int> pii;

#define FOR(i,a,b) for(i=a;i<b;i++) 
#define RA(x) (x).begin(), (x).end()
#define REV(x) reverse(RA(x))
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
#define X first
#define Y second
#define MOD 1000000007
int X, Y, dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};
bool vis[1000][1000];
string ans = "";
class node{
	public:
	string s;
	int x, y, k;
	node(int x, int y, int k, string s):x(x), y(y), k(k), s(s){}
};
int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int t=1, test;
	cin >> t;
	FOR(test, 0, t){
		ans = "";
		queue< node > q;
		memset(vis, 0, sizeof vis);
		cin >> X >> Y;
		X += 500; Y += 500;
		node n(500, 500, 0, "");
		q.push(n);
		while(!q.empty()){
			node n = q.front();
			q.pop();
			//cout << n.x << " " << n.y << endl;
			if(n.x == X && n.y == Y ){
				ans = n.s;
				break;
			}
			if(n.x < 0 || n.x > 1000 || n.y < 0 || n.y > 1000 || vis[n.x][n.y]) continue;
			vis[n.x][n.y] = 1;
			n.k++;
			q.push(node(n.x + n.k, n.y, n.k, n.s+'E'));
			q.push(node(n.x, n.y + n.k, n.k, n.s+'N'));
			q.push(node(n.x - n.k, n.y, n.k, n.s+'W'));
			q.push(node(n.x, n.y - n.k, n.k, n.s+'S'));
		}
		printf("Case #%d: %s\n", test+1, ans.c_str());
	}
}

