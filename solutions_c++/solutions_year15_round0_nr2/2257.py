#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <iomanip>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <stack>
#include <bitset>
#include <algorithm>
#include <math.h>
#include <sstream>
#pragma comment (linker, "/STACK:167177216")
using namespace std;
#define mems(A, val) memset(A, val, sizeof(A))
#define mp(a, b) make_pair(a, b)
#define all(B) (B).begin(), (B).end()
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define forit (it, coll) for( it = coll.begin(); it != coll.end(); ++it)
const int MAXN = 9;
typedef long long LL;

int d[1005][10005];


int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);


	mems(d, 1);
	d[2][1] = 1;
	d[1][1] = 0;
	d[2][2] = 0;
	d[0][0] = 0;
	for (int i = 3; i < 1005; i++)
	{
		d[i][i] = 0;
		for (int j = 1; j < i; j++)
		{
			for (int k = j; k < i; k++)
			{
				int temp = d[k][j];
				if (i - k > j) temp += d[i - k][j];
				d[i][j] = min(temp + 1, d[i][j]);
			}				
		}
	}




	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++)
	{
		int n;
		scanf("%d", &n);
		vector<int> st;
		for (int i = 0; i < n; i++)
		{
			int temp;
			scanf("%d", &temp);
			st.push_back(-temp);
		}
		
		sort(st.begin(), st.end());

		int ans = -st[0];
		for (int i = 1; i < -st[0]; i++)
		{
			int j = 0;
			int tans = i;
			while (j < st.size() && -st[j] > i)
			{
				tans += d[-st[j]][i];
				j++;
			}
			ans = min(tans, ans);
		}
	


		cout << "Case #" << test << ": " << ans << endl;
	}



    return 0;
}