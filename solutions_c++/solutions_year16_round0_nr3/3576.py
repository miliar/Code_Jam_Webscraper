#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

#define ll long long
#define INF 0x3f3f3f3f
#define LL_INF 0x3f3f3f3f3f3f3f3f
#define MAX 100

vector<ll> bases(char str[])
{
	vector<ll> vl;
	int len = strlen(str);
	for (int i = 2; i <= 10; ++i) {
		ll tmp = 0, t = 1;
		for (int j = len - 1; j >= 0; --j) {
			tmp += t * (str[j] - '0');
			t *= i;
		}
		vl.push_back(tmp);
	}
	return vl;
}

vector<ll> divisors(char str[])
{
	vector<ll> num = bases(str);
	vector<ll> divi;
	int len = num.size();
	ll nm = num[0];
	for (int i = 0; i < len; ++i) {
		ll tmp = num[i];
		bool flag = 0;
		for (ll j = 2; j <= nm; ++j) {
			if (tmp % j == 0 && j != tmp) {
				flag = 1;
				divi.push_back(j);
				break;
			}
		}
		if (!flag) {
			vector<ll> ddd;
			ddd.push_back(-1);
			return ddd;
		}
	}
	return divi;
}

int main()
{
	//freopen("debug\\in.txt", "r", stdin);
	//freopen("CON", "w", stdout);
	int i, j, k;
	int test, kase = 1;
	scanf("%d", &test);
	while (test--) {
		int N, J;
		scanf("%d%d", &N, &J);
		ll num = 1;
		for (j = 0; j < N-1; ++j) num *= 2;
		num += 1;
		//printf("%lld\n", num);
		int ans = 0;
		ll ddd = num + 10;
		printf("Case #%d:\n", kase++);
		for ( ; ; num++) {
			//printf("aa\n");
			char str[40];
			i = 0;
			memset(str, '\0', sizeof(str));
			//while (str[i++] != '\0') str[i-1] = '\0';
			int l = N - 1;
			ll nmp = num;
			//printf("%s\n", str);
			while (nmp >= 2) {
				//printf("bb\n");
				str[l--] = (nmp % 2 + '0');
				nmp /= 2;
			}
			str[0] = (nmp + '0');
			//printf("%s %d\n", str, strlen(str));
			vector<ll> vp = divisors(str);
			//printf("cc\n");
			if (vp[0] != -1 && str[0] != '0' && str[N - 1] != '0') {
				printf("%s ", str);
				for (i = 0; i < vp.size(); ++i)
					printf("%lld ", vp[i]);
				printf("\n");
				ans++;
				//printf("%d\n", ans);
			}
			//printf("J: %d\n", J);
			if (ans == J) break;
		}
	}
	return 0;
}