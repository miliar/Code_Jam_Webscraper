#include <queue>
#include <iostream>       
#include <string>
#include <vector>
#include <fstream>        
#include <functional> 
#include <algorithm>  
#include <cstdlib>    
#include <cstring>    
#include <map>        
#include <iomanip>    
#include <limits> 
#include <unordered_map>
#include <set>
#include <cmath>
#include <numeric> //accumulate
#include <stack>

//#include <unordered_set>//unordered_set

#define rep(i,a) for (int i = 0; i < (a); ++i)
#define rep2(i,a,b) for (int i = (a); i < (b); ++i)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define PI 3.14159265359;

using namespace std;
typedef long long ll;
typedef double lf;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<pair<int, int> > vpii;
typedef vector<vector<int> > vvi;
typedef const vector<int> cvi;
typedef vector<bool> vb;


int swapBits(int x, int i, int j) {
	int lo = ((x >> i) & 1);
	int hi = ((x >> j) & 1);
	if (lo ^ hi)
		x ^= ((1 << i) | (1 << j));
	return x;
}
int reverseXor(int x, int len) {
	int n = len;
	for (int i = 0; i < n / 2; ++i)
		x = swapBits(x, i, n - i - 1);
	return x;
}
vi getAdj(int state, int len) {
	vi ret;
	int tmp = 0;
	for (int i = 0; i < len; ++i) {
		tmp += (state & (1 << i));
		int invTmp = ~tmp;
		int revTmp = reverseXor(invTmp, i + 1);
		revTmp = revTmp & ((1 << (i + 1)) - 1);
		int pushItem = state & (((1 << 30) - 1) - ((1 << (i + 1)) - 1));
		pushItem += revTmp;
		ret.push_back(pushItem);
	}
	return ret;
}
map<int, int> stateMap;
void precalc() {
	stateMap[0] = 0;
	queue<int> q;
	q.push(0);
	while (!q.empty()) {
		int here = q.front();
		q.pop();
		int cost = stateMap[here];
		vi adj = getAdj(here, 11);	//10으로도 충분한데 그냥 안정성으로
		rep(i,adj.size())
			if (stateMap.count(adj[i]) == 0) {
				int there = adj[i];
				stateMap[there] = cost + 1;
				q.push(there);
			}
	}
}
int stringToInt(string str) {
	int ret = 0;
	int add = 1;
	rep(i, str.size()) {
		if (str[i] == '-')
			ret += add;
		add *= 2;
	}
	return ret;
}
string intToString(int num) {
	string ret;
	for (; num; num /= 2)
		if (num % 2)
			ret.push_back('-');
		else
			ret.push_back('+');
	//reverse(ret.begin(), ret.end());
	return ret;
}
long long getGreedy(string str) {
	long long ret = 0;
	char prevC = str[0];
	rep2(i, 1, str.size()) {
		if (prevC != str[i]) {
			ret++;
			prevC = str[i];
		}
	}
	if (str.back() == '-')
		ret++;
	return ret;
}
int main() {
	FILE* fp;
	freopen_s(&fp, "B-large.in", "r", stdin);
	freopen_s(&fp, "output.txt", "w", stdout);
	precalc();
	/*
	for (int num = 1; num < 2048; ++num) {
		string str = intToString(num);
		int sol1 = stateMap[num];
		int sol2 = getGreedy(str);
		if (sol1 != sol2)
			cout << "not Equal!!!: " << sol1 << sol2 << endl;
		else
			cout << "num: " << num << ", sol: " << sol1 << endl;
	}
	*/
	int T; cin >> T;
	rep(cc, T) {
		string str; cin >> str;
		int state = stringToInt(str);
		//int sol1 = stateMap[state];
		int sol2 = getGreedy(str);
		//if (sol1 != sol2)
		//	cout << "not Equal!!!!" << endl;
		//else
			cout << "Case #" << cc + 1 << ": " << sol2 << endl;
	}
	return 0;
}