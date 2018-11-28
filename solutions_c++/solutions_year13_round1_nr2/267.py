#include <bits/stdc++.h>

using namespace std;

#define MAXN 10005

long long E, R, N;

int v[MAXN];
int M[MAXN][20];

long long ans;

void solve(int p, int q, long long ei, long long ef)
{
	int k = 0;
	while( (1<<(k + 1)) <= q - p + 1) k++;
	
	int t;
	if(v[M[p][k]] > v[M[q - (1<<k) + 1][k]]) t = M[p][k];
	else t = M[q - (1<<k) + 1][k];
	
	long long to_recover = min(E, (q - t + 1) * R);
	long long need = max(ef - to_recover, 0LL);
	long long to_receive = min(E, ei + (t - p) * R);
	long long to_use = to_receive - need;
	
	ans += v[t] * to_use;
	
	if(p <= t - 1) solve(p, t - 1, ei, to_receive);
	if(t + 1 <= q) solve(t + 1, q, min(E, to_receive - to_use + R), ef);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		cin>>E>>R>>N;
		
		R = min(R, E);
		
		for(int i=0; i<N; i++)
			cin>>v[i];
		
		for(int i = 0; i < N; i++)
			M[i][0] = i;
		
		for(int j = 1; (1 << j) <= N; j++)
			for(int i = 0; i + (1 << j) - 1 < N; i++)
				if (v[M[i][j - 1]] > v[M[i + (1 << (j - 1))][j - 1]])
					M[i][j] = M[i][j - 1];
				else
					M[i][j] = M[i + (1 << (j - 1))][j - 1];
        
        ans = 0;
        solve(0, N-1, E, R);
        
		cout<<"Case #"<<caso<<": "<<ans<<endl;
	}
	
	return 0;
}
