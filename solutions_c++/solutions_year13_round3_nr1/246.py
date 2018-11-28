#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

typedef long long ll;

int T;
char ret[1000005];
int L;
int n;
ll pocet;
int za[1000005];
int vyh;

int main()
{
	scanf("%d\n", &T);

	for(int q=1; q<=T; q++) {
		scanf("%s %d\n", ret, &n);
		L=strlen(ret);
		pocet=0;
		za[L]=0;
		for(int i=L-1; i>=0; i--) {
			if(ret[i]!='a' && ret[i]!='e' && ret[i]!='i' && ret[i]!='o' && ret[i]!='u') za[i]=1+za[i+1];
			else za[i]=0;
		}
		vyh=(za[L-1]>=n ? L-1 : L);
		pocet+=L-vyh;
		for(int i=L-2; i>=0; i--) {
			vyh=min(vyh, (za[i]>=n ? i+n-1 : L));
			pocet+=(ll)(L-vyh);
		}
		printf("Case #%d: %lld\n", q, pocet);
	}

	return 0;
}
