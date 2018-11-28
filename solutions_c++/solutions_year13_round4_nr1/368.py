#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <sstream>
#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <LL> VL;

const int MAXN = 5010;
const int mod = 1000002013;

int A[MAXN], B[MAXN], C[MAXN];
int S[MAXN * 10], sn;
LL cnt[MAXN];
LL N;
int M;

int getID(int key)
{
	return lower_bound(S, S + sn, key) - S;	
}

LL dfs(int l, int r, LL dv)
{
	if(r <= l)	return 0;
	
	LL minV = 1LL << 60;
	for(int i = l; i <= r; ++ i)	
	{
		if(cnt[i] < minV)
		{
			minV = cnt[i];	
		}	
	}
	
	LL n = (S[r / 2] - S[l / 2]);
	LL ret = (n * N - n * (n - 1) / 2) % mod * (minV - dv) % mod;
	
//	cout << "lrr  " <<  l << " " << r << " " << minV << " " << ret << endl;
	
	int pre = l;
	for(int i = l; i <= r + 1; ++ i)
	{
		if(cnt[i] == minV || i == r + 1)
		{
			ret = (ret + dfs(pre, i - 1, minV)) % mod;
			pre = i + 1;	
		}	
	}
	
	return ret;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	

	int T;	cin >> T;
	
	for(int cas = 1; cas <= T; ++ cas)
	{
		cin >> N >> M;
		sn = 0;
		LL ans = 0;
		for(int i = 0; i < M; ++ i)
		{
			cin >> A[i] >> B[i] >> C[i];
			LL n = B[i] - A[i];
			ans += (n * N - n * (n - 1) / 2) % mod * C[i] % mod;
			S[sn ++] = A[i];
			S[sn ++] = B[i];
		}
		
//		cout << " " << ans << endl;
		
		sort(S, S + sn);
		sn = unique(S, S + sn) - S;
		
		
		memset(cnt, 0, sizeof(cnt));
		for(int i = 0; i < M; ++ i)
		{
			A[i] = getID(A[i]);
			B[i] = getID(B[i]);
			cnt[2 * A[i]] += C[i];
			cnt[2 * B[i] + 1] -= C[i];	
		}
		
		for(int i = 1; i < 2 * sn; ++ i)
		{
			cnt[i] += cnt[i - 1];	
		}
//		for(int i = 0; i < 2*sn; ++ i)	cout << cnt[i] << " ";cout << endl;
//		sort(A, A + M);
		
		cout << "Case #" << cas << ": " << (ans + mod - dfs(0, 2*sn - 1, 0)) % mod << endl;
	}
	
	
	return 0;	
}
