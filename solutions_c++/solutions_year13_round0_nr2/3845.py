#include <cstdio>
using namespace std;

bool run()
{
	int n, m;
	scanf("%d%d", &n, &m);
	int map[100][100];
	for(int i=0; i<n; i++) for(int j=0; j<m; j++)
		scanf("%d", &map[i][j]);
	for(int i=0; i<n; i++) for(int j=0; j<m; j++)
	{
		bool fx = true, fy = true;
		for(int k=i; k>=0; k--)
			if(map[k][j]>map[i][j]) fx = false;
		for(int k=i; k<n; k++)
			if(map[k][j]>map[i][j]) fx = false;
		for(int k=j; k>=0; k--)
			if(map[i][k]>map[i][j]) fy = false;
		for(int k=j; k<m; k++)
			if(map[i][k]>map[i][j]) fy = false;
		if(!(fx || fy)) return false;
	}
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
		if(run()) printf("Case #%d: YES\n", t);
		else printf("Case #%d: NO\n", t);
	return 0;
}

