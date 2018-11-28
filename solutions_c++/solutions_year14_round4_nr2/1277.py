#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <map>

using namespace std;

int N[1005], M[1005];
int Abs(int x) { return x < 0 ? -x : x; }

int D[1005];
int work(int n)
{
	int ans = 0;
	for (int i = 1; i <= n; i++) D[i] = N[i];
	for (int i = 1; i <= n; i++)
	{
		int tt = i;
		while (D[tt] != M[i]) tt++;
		for (int j = tt; j > i; j--) swap(D[j], D[j - 1]), ans++;
	}

	return ans;
}

int main()
{
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	int cas, T;
	
	for (cas = scanf("%d", &T); cas <= T; cas++)
	{
		int n;
		cin >> n;
		
		for (int i = 1; i <= n; i++) cin >> N[i];
		
		map <int, int> mm;
		map <int, int> :: iterator it;
		for (int i = 1; i <= n; i++) mm[N[i]] = 1;
		
		int id = 0;
		for (it = mm.begin(); it != mm.end(); it++) it -> second = ++id;
		for (int i = 1; i <= n; i++) N[i] = mm[N[i]];
		
		vector <int> vv;
		for (int i = 1; i <= n; i++) vv.push_back(i);
		
		int ans = 10000000;
		do {
			int now = 0, mark = 0;
			for (int i = 1; i < n; i++) if (vv[now] < vv[i]) now = i;
			for (int i = 0; i < now; i++) if (vv[i] > vv[i + 1]) mark = 1;
			for (int i = now + 1; i < n; i++) if (vv[i - 1] < vv[i]) mark = 1;
			if (mark) continue ;
			
			for (int i = 1; i <= n; i++) M[i] = vv[i - 1];
			ans = min(ans, work(n));
		}	while(next_permutation(vv.begin(), vv.end())) ;
		
		printf("Case #%d: ", cas);
		cout << ans << endl;
	}
	
	return 0;
}
