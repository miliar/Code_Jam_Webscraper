#include<iostream>
#include<cstdio>
#include<set>
#include<cstdlib>
#include<vector>
using namespace std;

#define FOR(x,N) for(int x = 0 ; x < (N) ; x++ )

int main()
{
	long long T;
	char buf[1000000];
	freopen("in2.in", "rt", stdin);
	freopen("out2.txt", "wt", stdout);

	cin >> T;
	string S, S2;
	FOR(i, T)
	{
		cin >> buf;
		S.clear();
		S = buf;		
		S2.clear();
		FOR(j, S.length())
		{
			if (j == 0)
			{
				S2[0] = S[0];
			}
			if (S2[0] > S[j] && j > 0)
			{
				S2 = S2 + S[j];
			}
			else if (S2[0] <= S[j])
			{
				S2 = S[j] + S2;
			}
		}

		cout << "Case #"<<i+1<<": "<< S2.c_str() << endl;

	}

	return 0;
}
