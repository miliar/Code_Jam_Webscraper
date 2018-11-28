#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int n, r, p, s;

void doit(int n, int r, int p, int s){
	if (n==1){
		if (p>0) printf("P");
		if (r>0) printf("R");
		if (s>0) printf("S");
		return;
	}

	int nn = (1<<(n-1)), i, j, k, ii, jj, kk;
	bool yes = false;
	for (i=p; i>=0; i--){
	for (j=i-1; j<=s; j++){
		if (j<0) continue;
		k = nn - i- j;
		if (k < 0) break;
		ii = p-i;
		jj = s-j;
		kk = r-k;

		//cout<<"try "<<k<<' '<<i<<' '<<j<<endl;
		//cout<<"   "<<kk<<' '<<ii<<' '<<jj<<endl;
		
		if (k-i>1 || i-j>1 || j-k>1 || kk-ii>1 || ii-jj>1 || jj-kk>1){
			continue;
		}

		yes = true;
		break;
	}
	if (yes) break;
	}

	if (yes){
		doit(n-1, k, i, j);
		doit(n-1, kk, ii, jj);
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("large.out","w",stdout);
	
	int task; scanf("%d", &task);
	for (int cs=1; cs<=task; cs++){
		scanf("%d%d%d%d", &n, &r, &p, &s);
		printf("Case #%d: ", cs);
		if (r-p>1 || p-s>1 || s-r >1){
			printf("IMPOSSIBLE\n");
			continue;
		}

		doit(n, r, p, s);
		printf("\n");
	}	

	return 0;
}
