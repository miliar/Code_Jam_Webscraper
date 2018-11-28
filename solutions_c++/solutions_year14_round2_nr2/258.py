#include <bits/stdc++.h>

using namespace std;

int A, B, K;

bool check(int n, int p)
{
	return (n & (1<<p)) != 0;
}

long long memo[30][2][2][2];

long long f(int p, bool fA, bool fB, bool fK)
{
	if(p == -1) return 1;
	
	if(memo[p][fA][fB][fK] != -1)
		return memo[p][fA][fB][fK];
	
	long long ans = 0;
	
	ans += f(p - 1, (check(A, p) ? 1 : fA), (check(B, p) ? 1 : fB),
					(check(K, p) ? 1 : fK));
	
	if(fA || check(A, p)){
		ans += f(p - 1, fA, (check(B, p) ? 1 : fB),
						    (check(K, p) ? 1 : fK));
	}
	
	if(fB || check(B, p)){
		ans += f(p - 1, (check(A, p) ? 1 : fA), fB,
						(check(K, p) ? 1 : fK));
	}
	
	if((fK || check(K, p)) && (fA || check(A, p)) && (fB || check(B, p))){
		ans += f(p - 1, fA, fB,	fK);	
	}
	
	memo[p][fA][fB][fK] = ans;
	return ans;
}

int main()
{
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		cin>>A>>B>>K;
		A--;
		B--;
		K--;
		
		memset(memo, -1, sizeof(memo));
		cout<<"Case #"<<caso<<": "<<f(29, 0, 0, 0)<<endl;	
	}
  
	return 0;
}
