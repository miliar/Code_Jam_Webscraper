#include <iostream>
#include <string>
#include <vector>

using namespace std;

int countbit( int n ) { int c=0; while(n)c+=n&1,n>>=1; return c; }

vector<double> table(int n)
{
	vector<double> T(1<<n);

	for ( int b=n-1; b>=0; b-- )
	for ( int i=0; i<(1<<n); i++ )
	if ( countbit(i)==b )
	{
		for ( int j=0; j<n; j++ )
		{
			int c;
			for (c=0; i>>((j+c)%n)&1; c++ )
				;
			T[i] += (n-c)+T[i|1<<((j+c)%n)];
		}
		T[i] /= n;
	}
	return T;
}

int main()
{
	const int N = 20;
	vector<double> S[N+1];

	for ( int i=1; i<=N; i++ )
		S[i] = table(i);

	int T;
	cin>>T;
	for ( int test=1; test<=T; test++ )
	{
		string s;
		cin>>s;
		int t=0;
		for ( int i=0; i<(int)s.size(); i++ )
			t = 2*t + (s[s.size()-i-1]=='X'?1:0);
		printf("Case #%d: %.20f\n",test,S[s.size()][t]);
	}
	return 0;
}