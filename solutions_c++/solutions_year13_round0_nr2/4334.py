#include<cstdio>
#include<cstdlib>

int s[100][100];
int x[100], y[100];
int n, m;
bool check()
{
	bool out = true;
	for(int i=0; i<n; i++) {
		x[i] = 0;
		for(int j=0; j<m; j++) if (s[i][j] > x[i]) x[i] = s[i][j];
	}
	for(int i=0; i<m; i++) {
		y[i] = 0;
		for(int j=0; j<n; j++) if (s[j][i] > y[i]) y[i] = s[j][i];
	}
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) if (s[i][j] < x[i] && s[i][j] < y[j]) return false;
	}

	return true;
}

int main()
{
	freopen("B-large.in", "r",stdin);
	freopen("B.out", "w",stdout);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++) {
		scanf("%d%d" ,&n, &m);
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++) scanf("%d", &s[i][j]);
		if (check()) 
			printf("Case #%d: YES\n", t);
		else 
			printf("Case #%d: NO\n", t);

	}
	return 0;
}
