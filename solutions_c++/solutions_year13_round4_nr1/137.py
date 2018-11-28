#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>

using namespace std;

vector< pair<long long, long long> > A;
vector< long long > B;
stack< pair<long long, long long> > S;
stack< long long > SS;

int T;
long long N;
int M;
long long ret;
long long MOD = 1000002013;
long long TWO = 2;

int main(void)
{
	int l0, l1, l2, l3;

	cin >> T;
	for(l0 = 1; l0 <= T; l0++)
	{
		cin >> N >> M;
		A.clear();
		B.clear();
		while(!S.empty()) S.pop();
		for(l1 = 0; l1 < M; l1++)
		{
			long long v1, v2, v3;
			cin >> v1 >> v2 >> v3;
			A.push_back( make_pair(v1, -v3) );
			B.push_back( v2 );
			A.push_back( make_pair(v2, v3) );
			B.push_back( -1 );
		}

		for(l1 = 0; l1 < (int)A.size(); l1++)
		{
			for(l2 = l1+1; l2 < (int)A.size(); l2++)
			{
				if(A[l1] > A[l2])
				{
					swap(A[l1], A[l2]);
					swap(B[l1], B[l2]);
				}
			}
		}

		ret = 0;
		for(l1 = 0; l1 < (int)A.size(); l1++)
		{
			if(A[l1].second < 0) // push
			{
				S.push( make_pair(A[l1].first, -A[l1].second) );
				SS.push( B[l1] );
			}
			else
			{
				while(A[l1].second > 0)
				{
					if(S.top().second == 0)
					{
						S.pop();
						SS.pop();
					}
					else
					{
						long long delta = 0;
						long long origi = 0;
						long long weight = 0;
						if(S.top().second >= A[l1].second)
						{
							delta = A[l1].first - S.top().first;
							origi = SS.top() - S.top().first;
							weight = A[l1].second;
						}
						else
						{
							delta = A[l1].first - S.top().first;
							origi = SS.top() - S.top().first;
							weight = S.top().second;
						}

						S.top().second -= weight;
						A[l1].second -= weight;

						long long value1 = origi * N - origi * (origi - 1) / TWO;
						long long value2 = delta * N - delta * (delta - 1) / TWO;

						long long value = (value1 - value2) % MOD;
						value = (value + MOD) % MOD;
						value *= weight;
						value %= MOD;

						ret = (ret + value) % MOD;
					}
				}
			}
		}

		cout << "Case #" << l0 << ": " << ret << endl;
	}
}
