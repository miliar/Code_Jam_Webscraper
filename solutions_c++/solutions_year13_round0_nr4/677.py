// esta3anna 3al sha2a belAllah ..
#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<limits.h>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std ;
#define rep(i,n,m) for(int i = (int)(n), _m = (int)(m); i < _m; ++ i)
#define	rrep(i,n,m) for(int i = (int)(n), _m = (int)(m); i >= _m; -- i)
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define mems(arr, v) memset(arr, v, sizeof arr)
#define setBit(mask, bit) ((mask) | (1LL << (bit)))
#define resetBit(mask, bit) ((mask) & (~(1LL << (bit))))
#define flipBit(mask, bit) ((mask) ^ (1LL << (bit)))
#define is0(mask, bit)(((mask) & (1LL << (bit))) == 0)
#define is1(mask, bit)(((mask) & (1LL << (bit))) != 0)
#define removeLastBit(mask) ((mask) & ((mask) - 1LL))
#define firstBitOn(mask) ((mask) & ~((mask) - 1LL))
#define grayCode(mask) ((mask) ^ ((mask) << 1LL))
#define repSubMasks(subMask, mask) for(ll subMask = (ll)(mask), _mask = subMask; subMask; subMask = _mask & (subMask - 1))
int countBits(int mask) {int res = 0; while(mask) mask &= (mask - 1), ++ res; return res;}
#define INT_MAX  2000000000
#define INT_MIN -INT_MAX
#define EPS 1e-9
#define debug(x) cout << #x << " : " << x << endl
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
#define Read() freopen("input.txt","r",stdin)
#define Write() freopen("output.txt","w",stdout)
int n;
int dp[1 << 20];
int key[301];
int keys[301][301];
int freq[301];
bool can(int mask, int k) {
	int currFreq = freq[k];
	rep(i, 0, n)
		if(mask & (1 << i))
			currFreq += (keys[i][k]) - (key[i] == k);
	return currFreq > 0;
}
bool rec(int mask) {
	if(mask == (1 << n) - 1)
		return dp[mask] = true;
	if(dp[mask] != -1)
		return dp[mask];
	rep(i, 0, n)
		if((mask & (1 << i)) == 0)
			if(can(mask, key[i]))
				if(rec(mask | (1 << i)))
					return dp[mask] = true;
	return dp[mask] = false;
}
void print(int mask) {
	if(mask == (1 << n) - 1) {
		puts("");
		return;
	}
	rep(i, 0, n)
		if((mask & (1 << i)) == 0)
			if(can(mask, key[i]))
				if(dp[mask | (1 << i)]) {
					cout << ' ' << i + 1;
					print(mask | (1 << i));				
					return;
				}
}
int main() {
	Read();
	Write();
	int cases, m, tmp, k;
	cin >> cases;
	rep(C, 1, cases + 1) {
		cin >> k >> n;
		mems(freq, 0);
		mems(keys, 0);
		rep(i, 0, k) {
			cin >> tmp;
			++ freq[tmp];
		}
		rep(i, 0, n) {
			cin >> key[i];
			cin >> m;
			rep(j, 0, m) {
				cin >> tmp;
				++ keys[i][tmp];
			}
		}
		cout << "Case #" << C << ":";
		mems(dp, -1);
		if(!rec(0))
			cout << " IMPOSSIBLE" << endl;
		else {
			print(0);
		}
	}
}