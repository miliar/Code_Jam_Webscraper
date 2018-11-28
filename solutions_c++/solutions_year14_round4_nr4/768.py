#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

const int MAX_N = 107;
const int P = 1000000007;

int T, n, m;
long long ans = 0, ansm = 0, s[MAX_N];
vector<int> str[MAX_N];
string a[MAX_N];

int cpf[MAX_N][MAX_N];

int calc(int x) {
    if (n >= x) {
    	for (int i = 1; i <= m; ++i) {
    		s[x] = i;
    		calc(x + 1);
    	}
    	return 0x5942b;
	}
    int tmp = 0;
	for (int i = 1; i <= m; ++i)
	    str[i].clear();
	for (int i = 1; i <= n; ++i) 
        str[s[i]].push_back(i);
	for (int i = 1; i <= m; ++i) 
        if (str[i].size() == 0) return 0;
	for (int i = 1; i <= m; ++i) {
		++tmp;
		for(int j = 1; j <= str[i].size(); ++j) {
			tmp += a[str[i][j - 1]].length();
			int maxcpf = 0;
			for(int k = 1; k <= j - 1; ++k)
                maxcpf = max(maxcpf,cpf[str[i][k - 1]][str[i][j - 1]]);
			tmp -= maxcpf;
		}
	}
	if (tmp > ans) {
		ans = tmp;
        ansm = 1;
	} else if (tmp == ans) {
	    ++ansm;
	    ansm %= P;
	}
	return 0x5942b;
}
void work() {
    for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                int tt = min(a[i].length(), a[j].length());
    			cpf[i][j] = tt;
                for(int k = 1; k <= tt; ++k)
                    if (a[i][k - 1] != a[j][k - 1]) {
    				    cpf[i][j] = k - 1; 
                        break;
			        }
		    }
		}
}
int main() {
	freopen("D-small-attempt0.in", "r", stdin);
    freopen("dd.out", "w", stdout);
	cin >> T;
	for(int cs = 1; cs <= T; ++cs) {
		
		cin >> n >> m;
		for (int i = 1; i <= n; ++i)
            cin >> a[i];
		work();
        ans = 0;
        ansm = 0;
		calc(1);
		
		printf("Case #%d: %lld %lld\n",cs, ans, ansm % P);
	}
	return 0;
}

