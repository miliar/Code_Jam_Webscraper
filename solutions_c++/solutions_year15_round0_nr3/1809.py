/*
 * codejam-QR2015-C.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: ghooo
 */

#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>
//#include <windows.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);++i)
#define repe(i,n,m) for(int i=n;i<=(int)(m);++i)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define reset(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)
#define clrq(x) while(!x.empty()) x.pop();
#define clrvv(v) rep(i,sz(v))v[i].clear();
#define debug(x) cerr << #x << ": " << x << endl;
#define debugv(v) cerr << #v << ": ";For(it,v)cerr <<(*it)<<", "; cerr<<endl;

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;
typedef unsigned long long ull;
typedef long long ll;

//==============================================================
// handling triples
typedef pair<ll,pair<ll,ll> > triple;
#define tfirst first
#define tsecond second.first
#define tthird second.second
#define mt(x,y,z) mp(x,mp(y,z))
//---------------------------------------------------------------

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;
int mul[8][8];
// 0   1  2   3  4   5  6   7
// 1, -1, i, -i, j, -j, k, -k
void init(){
	// 1
	rep(i,8) mul[0][i]=i;
	// -1
	rep(i,8) mul[1][i]=i^1;
	// i
	mul[2][0]=2, mul[2][2]=1, mul[2][4]=6, mul[2][6]=5;
	for(int i = 1; i < 8; i+=2) mul[2][i]=mul[2][i-1]^1;
	// -i
	rep(i,8) mul[3][i]=mul[2][i]^1;
	// j
	mul[4][0]=4,mul[4][2]=7,mul[4][4]=1,mul[4][6]=2;
	for(int i = 1; i < 8; i+=2) mul[4][i]=mul[4][i-1]^1;
	// -j
	rep(i,8) mul[5][i]=mul[4][i]^1;
	// k
	mul[6][0]=6,mul[6][2]=4,mul[6][4]=3,mul[6][6]=1;
	for(int i = 1; i < 8; i+=2) mul[6][i]=mul[6][i-1]^1;
	// -k
	rep(i,8) mul[7][i]=mul[6][i]^1;

//	string dic[8];
//	dic[0]="1";
//	dic[1]="-1";
//	dic[2]="i";
//	dic[4]="j";
//	dic[6]="k";
//	dic[3]="-i";
//	dic[5]="-j";
//	dic[7]="-k";
//
//	cout << setw(4) << " " << "|";
//	rep(i,8) cout << setw(4) << dic[i];
//	cout << endl;
//	rep(i,9*4+1) cout << "-";
//	cout << endl;
//	rep(i,8){
//		cout << setw(4) << dic[i] << "|";
//
//		rep(j,8){
//			cout << setw(4) << dic[mul[i][j]];
//		}
//		cout << endl;
//	}
//	exit(0);
}

vector<int> gen(string&s, int n){
	int convert[128];
	convert[(int)'i']=2;
	convert[(int)'j']=4;
	convert[(int)'k']=6;
	vector<int> ret(sz(s)*n,'.');
	rep(i,sz(s))
		rep(j,n)
			ret[j*sz(s)+i]=convert[(int)s[i]];
	return ret;
}
int vis[10000*20][8][8],id;
bool dp[10000*20][8][8];
vector<int> v;
// ijk
bool rec(int idx, int prvVal, int target){
	if(idx == sz(v)) return prvVal==target&&target==6;
	if(target>6) return false;
	bool &ret = dp[idx][prvVal][target];
	if(vis[idx][prvVal][target]==id)return ret;
	vis[idx][prvVal][target]=id;
	int nxtVal = mul[prvVal][v[idx]];
	ret = rec(idx+1,nxtVal,target);
	if(nxtVal==target) ret |= rec(idx+1,0,target+2);
	return ret;
}
int fix(int n){
	int ret = n%4;
	while(ret+4<=20 && ret+4 <= n) ret+=4;
	return ret;
}
int main(){
	ios_base::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	init();

	int t;
	cin >> t;
	repe(tst,1,t){
		int l, x;
		string s;
		cin >> l >> x >> s;
		x = fix(x);
		x = min(20,x);
		v = gen(s,x);

		id++;

		cout << "Case #" << tst << ": ";
		if(rec(0,0,2))
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
