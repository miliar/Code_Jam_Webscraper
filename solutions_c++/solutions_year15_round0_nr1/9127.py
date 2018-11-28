#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <set>
#include <stack>
#include <functional>
using namespace std;
#define forn(i,n) for(int i = 0; i < n; i++)
#define forn2(i,j,n) for(int i = j; i <= n; i++)
#define forall(i,vec) for(typeof(vec.begin()) i = vec.begin(); i != vec.end(); i++)
#define pb(i) push_back(i)
#define mp(i,j) make_pair(i,j)
#define ON(mask,i) (mask | (1<<(i)))
#define isON(mask,i) (mask & (1<<(i)))
#define OFF(mask,i) (mask & (~(1<<(i))))

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;
const int INF = 1000000000;
const int MAXN = 100005;

int main(){
	int T,N;
	string s;
	cin >> T;
	forn2(t,1,T){
		cin >> N >> s;
		int tot = s[0] - '0', res = 0;
		forn2(i,1,N){
			if(tot < i){
				res += i - tot;
				tot = i;
			}
			tot += s[i] - '0';
		}
		cout << "Case #" << t << ": " << res << endl;
	}
}
