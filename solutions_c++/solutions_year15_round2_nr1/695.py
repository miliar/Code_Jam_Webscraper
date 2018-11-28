#include <algorithm>
#include <vector>
#include <string>
#include <ctime>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

//queue<pair<long long, long long > > q;
//set<long long> s;
//int ans0[1050];
//long long arr[1050];
//
//int par[10000005];

long long nm[16], rnm[16];
char nms[16][20], rnms[16][20];

//inline long long rev(long long num)
//{
//	long long numr = 0;
//	while (num)
//	{
//		numr *= 10;
//		numr += num % 10;
//		num /= 10;
//	}
//	return numr;
//}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output1.txt", "w", stdout);

	int t1 = clock();
	int T; 
	cin >> T;
	for (int tt = 0; tt < T; ++tt)
	{
		/*long long  n;
		cin >> n;

		arr[tt] = n;
		s.clear();
		while (!q.empty())
			q.pop();
		q.push(make_pair(n, 0));
		s.insert(n);
		long long ans = -1;

		while (true)
		{
			pair<long long, long long> p = q.front();
			q.pop();
			long long num = p.first, st = p.second;
			if (num == 1)
			{
				ans = st;
				break;
			}

			long long numr = rev(num);
			if (numr < num && rev(numr) == num && s.find(numr) == s.end())
			{
				q.push(make_pair(numr, st + 1));
				s.insert(numr);
				par[numr] = num;
			}

			num--;
			if (s.find(num) == s.end())
			{
				q.push(make_pair(num, st + 1));
				s.insert(num);
				par[num] = num + 1;
			}
			
			num++;
			
		}*/
		//printf("Case #%d: %lld\n", tt + 1, ans + 1);
		/*ans0[tt] = ans + 1;

		for (int x = 1; x < n; x = par[x])
			if (x != par[x] - 1)
				printf("%d %d\n", x, par[x]);
		cout << " !!!!" << endl;*/

		for (int i = 1; i < 16; ++i)
		{
			memset(nms[i], '0', i / 2);
			memset(nms[i] + i / 2, '9', (i + 1) / 2);
			nms[i][0] = '1';
			memcpy(rnms[i], nms[i], i);
			reverse(rnms[i], rnms[i] + i);

			sscanf(nms[i], "%lld", &nm[i]);
			sscanf(rnms[i], "%lld", &rnm[i]);
		}

		long long n;
		cin >> n;
		long long ans = 0, cur = 1;
		if (n % 10 == 0) 
			--n, ++ans;
		for (int i = 1;; ++i)
		{
			if (rnm[i] > n)
				break;
			ans += nm[i] - cur + 1;
			cur = rnm[i];
		}

		long long q = 0, pw = 1, nn = n;
		while (nn)
		{
			++q;
			pw *= 10;
			nn /= 10;
		}
		pw /= 10;
		if (pw > cur)
		{
			ans += pw - cur;
			long long mid = 0;
			long long pw1 = 1;
			for (int i = 0; i < q / 2; ++i)
				pw1 *= 10;
			long long n1 = n % pw1;
			ans += n1 - 1;
			n -= n1 - 1;

			long long rn = 0;
			long long nn = n;
			while (nn)
			{
				rn *= 10;
				rn += nn % 10;
				nn /= 10;
			}
			ans += rn - pw;
			if (rn < n)
				++ans;
		}
		else
			ans += n - cur;
		
		//cout << ans << endl;

		printf("Case #%d: %lld\n", tt + 1, ans);
	}
	//cout << clock() - t1 << endl;


	

	return 0;
}

/*

*/