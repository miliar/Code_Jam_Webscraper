#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

typedef long long ll;

const int N = 110;

int t, n, first[30], last[30], mid[30], alone[30], nex[30], a;
ll res, silnia[N], mod=1000000007;
char s[N];
bool T[N];

int main() {
	silnia[0] = 1;
	for(int i = 1; i <= 100; i++)
		silnia[i] = (silnia[i-1]*i)%mod;
	scanf("%d", &t);
	for(int c = 1; c <= t; c++) {
		for(int i = 0; i < 26; i++) {
			nex[i] = -1;
			memset(first, 0, sizeof(first));
			memset(last, 0, sizeof(last));
			memset(mid, 0, sizeof(mid));
			memset(alone, 0, sizeof(alone));
			memset(T, 0, sizeof(T));
		}
		scanf("%d", &n);
		for(int i = 0; i < n; i++) {
			res = 1;
			scanf("%s", s);
			int m = strlen(s);
			bool w = true;
			for(int j = 0; j < m; j++) {
				if(s[j]!=s[0])
					w = false;
			}
			if(w==true)
				alone[s[0]-'a']++;
			else {
				w = true;
				first[s[0]-'a']++;
				for(int j = 0; j < m; j++) {
					if(s[j]!=s[0])
						w = false;
					if(w==false && s[j]!=s[j-1])
						mid[s[j]-'a']++;
				}
				last[s[m-1]-'a']++;
				mid[s[m-1]-'a']--;
				nex[s[0]-'a'] = s[m-1]-'a';
			}
		}
		for(int j = 0; j < 26; j++) {
			if(mid[j]>1 || last[j]>1 || first[j]>1 ||
			(mid[j]==1 && (first[j]>0 || last[j]>0 || alone[j]>0)))
				res = 0;
		}
		bool ok = false;
		for(int j = 0; j < 26; j++) {
			if(!(first[j]==1 && last[j]==1))
				ok = true;
		}
		if(ok==false)
			res = 0;
		if(res==0) {
			printf("Case #%d: 0\n", c);
			continue;
		}
		for(int i = 0; i < 26; i++)
			res = (res*silnia[alone[i]])%mod;
		int x = 0;
		for(int i = 0; i < 26; i++) {
			if(first[i]==1 && last[i]==0) {
				x++;
				T[i] = true;
				a = nex[i];
				while(a!=-1) {
					T[a] = true;
					a = nex[a];
				}
			}
		}
		for(int i = 0; i < 26; i++) {
			if((first[i]>0 || last[i]>0) && T[i]==false) {
				res = 0;
				break;
			}
		}
		for(int i = 0; i < 26; i++) {
			if(alone[i]>0 && first[i]==0 && last[i]==0)
				x++;
		}
		res = (res*silnia[x])%mod;
		printf("Case #%d: %lld\n", c, res);
	}
	return 0;
}
