#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <vector>
using namespace std;

int T;
int n;
int a[12];

vector<int> perm;

int main()
{
	scanf("%d", &T);

	for(int q=1; q<=T; q++) {
		scanf("%d", &n);
		for(int i=0; i<n; i++) scanf("%d", &a[i]);
		perm.resize(n);
		for(int i=0; i<n; i++) perm[i]=i;
		int ans=1000000007;
		do {
			int pom[12];
			for(int i=0; i<n; i++) pom[i]=a[perm[i]];
			int j=0;
			while(j<n-1 && pom[j]<pom[j+1]) j++;
			while(j<n-1 && pom[j]>pom[j+1]) j++;
			int akt=0;
			for(int i=0; i<n; i++) {
				for(int j=i+1; j<n; j++) {
					if(perm[i]>perm[j]) akt++;
				}
			}
			if(j==n-1) ans=min(ans, akt);
		} while(next_permutation(perm.begin(), perm.end()));
		printf("Case #%d: %d\n", q, ans);
	}

	return 0;
}
