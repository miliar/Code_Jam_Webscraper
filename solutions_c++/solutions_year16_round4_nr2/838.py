#include<bits/stdc++.h>
using namespace std;
#define MAXN 210
double DP[MAXN][2*MAXN];
double sol;
double P[MAXN];
vector<double> prob;
int N,K;

double calcola()
{
	for(int j=0; j<MAXN; ++j)
		for(int i=0; i<2*MAXN; ++i)
			DP[j][i] = 0;

	DP[0][K+1] = prob[0];
	DP[0][K-1] = 1-prob[0];

	for(int i=1; i<K; ++i)
			for(int d=0; d<=2*K; ++d)
			{
				if(d>0)
					DP[i][d] += DP[i-1][d-1] * prob[i];
				if(d<2*K)
					DP[i][d] += DP[i-1][d+1] * (1 - prob[i]);
			}

	return DP[K-1][K];
}

void genera(int pos, int presi)
{
	if(pos == N)
	{
		if(presi != K) return;
		sol = max(sol, calcola());
		return;
	}
	
	genera(pos+1, presi);

	if(presi < K)
	{
		prob.push_back(P[pos]);
		genera(pos+1, presi+1);
		prob.pop_back();
	}
}


double foo()
{
	cin >> N >> K;
	for(int i=0;i<N; ++i)
		cin >> P[i];
	prob.clear();
	sol = 0;
	genera(0,0);
	return sol;
}

int main()
{
	int T;
	cin >> T;
	for(int i=0; i<T; ++i)
		cout << setprecision(20) << fixed << "Case #" << i+1 << ": " << foo() << "\n";
	return 0;
}
