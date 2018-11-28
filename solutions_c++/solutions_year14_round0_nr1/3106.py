#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstring>
#include <cctype>
#include <iomanip>
#include <fstream>
#include <ctime>
#define LL long long
#define ULL unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOD(i,a,b) for(int i=a;i>b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define fi first
#define se second
#define pb push_back
#define mp make_pair

using namespace std;

typedef pair<LL,int>II;
typedef pair<int,II>PII;
template<class T> T gcd(T a, T b) {T r; while(b!=0) {r=a%b;a=b;b=r;} return a;}
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }

const double PI = 2*acos(0.0);
const double eps = 1e-9;
const int infi = 2e9;
const LL Linfi = (LL) 1e18;
#define MOD 1000000007
#define maxn 100005


int x,y, a[5][5], b[5][5];

void thuchien(){
	int ans = -1, cnt = 0;
	FOR(i,1,4) FOR(j,1,4){
		if(a[x][i] == b[y][j]) {
			cnt++;
			ans = a[x][i];
		}
	}
	//cout << cnt << " ";
	if(cnt == 1) cout << ans << endl;
	else if(cnt >= 2) cout << "Bad magician!" << endl;
	else cout << "Volunteer cheated!" << endl;
}

int main(){
    //std::ios::sync_with_stdio(0);

    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    int sotest = 0;
    cin >> sotest;
    FOR(test,1,sotest){
		cin >> x;
		FOR(i,1,4) FOR(j,1,4) cin >> a[i][j];
		cin >> y;
		FOR(i,1,4) FOR(j,1,4) cin >> b[i][j];
		cout << "Case #" << test << ": ";
		thuchien();
    }
    return 0;
}


