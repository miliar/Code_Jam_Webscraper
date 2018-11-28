#include <stdio.h>
#include <algorithm>
using namespace std;

#define BIG_GRASS 110

int t;
int n,m;
int pat[110][110];
int gr[110][110];

pair<int,int> lookForBig() {
	int big=0;
	pair<int,int> ans=make_pair(-1,-1);

	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
			if (gr[i][j]>pat[i][j] && big<pat[i][j])
				big=pat[i][j], ans=make_pair(i,j);
	return ans;
}

bool tryMown(int i, int j) {
	int max_e=0;
	if (i==-1 && j==-1)
		return false;

	for (int k=0; k<n; k++)
		max_e=max(max_e,pat[k][j]);
	
	if (max_e==pat[i][j]) {
		for (int k=0; k<n; k++)
			gr[k][j]=max_e;
		return true;
	}

	max_e=0;
	for (int k=0; k<m; k++)
		max_e=max(max_e,pat[i][k]);
	
	if (max_e>pat[i][j])
		return false;

	for (int k=0; k<m; k++)
		gr[i][k]=max_e;
	return true;
}

bool reachPat() {
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
			if (pat[i][j]!=gr[i][j])
				return false;
	return true;
}

int main() {
	scanf("%d", &t);
	
	for (int casen=1; casen<=t; casen++) {
		scanf("%d %d", &n,&m);
		
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
				scanf("%d", &pat[i][j]);

		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
				gr[i][j]=BIG_GRASS;
		pair<int,int> big;

		do {
			big=lookForBig();
		} while (tryMown(big.first, big.second));

		printf("Case #%d: %s\n", casen,reachPat()? "YES":"NO");
	}
	return 0;
}
