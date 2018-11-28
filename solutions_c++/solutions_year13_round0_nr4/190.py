#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std;
#define setb(mask, bit) (mask|((1LL)<<bit))
#define resetb(mask, bit) (mask&(~((1LL)<<bit)))
#define is0(mask, bit)((mask&((1LL)<<bit))==0)
#define is1(mask, bit)((mask&((1LL)<<bit))!=0)
#define MAX_N 21
#define MAX_KEYS 50
#define MAX_CHEST_TYPES 201
#define MAX_KEYS_TYPES 201
int N, K;
int keyNeeded[MAX_N];
int initKeys[MAX_KEYS];
vector< vector<int> > chestKeys;
int dp[1 << 20];
bool yes(int mask)
{
	if(mask == (1 << N) - 1)
		return true;
	if(dp[mask] != -1)
		return dp[mask];
	int freq[MAX_KEYS_TYPES] = {};
	for(int i = 0; i < K; ++i)
		++freq[initKeys[i]];
	for(int i = 0; i < N; ++i)
	{
		if(is1(mask, i))
		{
			for(int j = 0; j < chestKeys[i].size(); ++j)
				++freq[chestKeys[i][j]];
			--freq[keyNeeded[i]];
		}
	}
	dp[mask] = false;
	for(int i = 0; i < N; ++i)
	{
		if(is0(mask, i) && freq[keyNeeded[i]])
		{
			dp[mask] |= yes(setb(mask, i));
			if(dp[mask])
				break;
		}
	}
	return dp[mask];
}
void print(int mask)
{
	if(mask == 0)
		return;
	for(int i = 0; i < N; ++i)
	{
		if(is0(mask, i))
			continue;
		if(dp[resetb(mask, i)] == 1)
		{
			print(resetb(mask, i));
			cout << " " << i + 1;
			return;
		}
	}
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for(int ti = 1; ti <= T; ++ti)
	{
		memset(dp, -1, sizeof dp);
		cin >> K >> N;
		chestKeys.clear();
		chestKeys.resize(N);
		for(int i = 0; i < K; ++i)
			cin >> initKeys[i];
		int ki, a;
		for(int i = 0; i < N; ++i)
		{
			cin >> keyNeeded[i];
			cin >> ki;
			for(int j = 0; j < ki; ++j)
			{
				cin >> a;
				chestKeys[i].push_back(a);
			}
		}
		cout << "Case #" << ti << ":";
		if(!yes(0))
			cout << " IMPOSSIBLE\n";
		else
		{
			print((1 << N) - 1);
			cout << endl;
		}
	}
}