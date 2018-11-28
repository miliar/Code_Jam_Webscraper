#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <map>

using namespace std;

char str[100010];
vector<string>ans_str;
vector<long long>ans;
vector<long long>store;
int main(int argc, char const *argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T = 0;
	int cas = 0;
	scanf("%d", &T);
	while(T--) {
		cas++;
		printf("Case #%d:\n", cas);
		int N, J;
		scanf("%d%d", &N, &J);
		for(long long sta = (1ll << (N - 1)) + 1; sta < (1ll<<N); sta += 2) {
			long long tmp = sta;
			//printf("%lld\n", sta);
			bool fg = 1;
			string s;
			while(tmp) {
				if(tmp & 1) {
					s += '1';
				} else {
					s += '0';
				}
				tmp >>= 1;
			}
			store.clear();
			for(int b = 2; b <= 10; b++) {
				tmp = sta;
				long long now = 1;
				long long val = 0;
				long long dv;
				if(b & 1) {
					dv = 2;
				} else {
					dv = b + 1;
				}
				for(int i = 0; i < N; i++) {
					val += (s[i] == '1') * now;
					now *= b;
					now %= dv;
					val %= dv;
					tmp >>= 1;
					//printf("%lld & %lld\n", val, now);
				}
				if(val % dv == 0) {
					store.push_back(dv);
				} else {
					fg = 0;
					break;
				}
			}

			for(int i = 0; i < N - i - 1; i++) {
				swap(s[i], s[N - i - 1]);
			}

			if(fg) {
				ans_str.push_back(s);
				//printf("%d\n", ans_str.size());
				for(int i = 2; i <= 10; i++) {
					ans.push_back(store[i - 2]);
				}
				if(ans_str.size() == J) {
					break;
				}
			}
		}
		int pos = 0;
		for(int i = 0; i < J; i++) {
			printf("%s", ans_str[i].c_str());
			for(int j = 0; j < 9; j++) {
				printf(" %lld", ans[pos++]);
			}
			puts("");
		}
	}
	return 0;
}