#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin>>T;

	for (int i = 0; i < T; ++i)
	{
		int A,N;
		cin>>A>>N;

		vector<int> vi;
		for (int j = 0; j < N; ++j)
		{
			int tmp;
			cin>>tmp;
			vi.push_back(tmp);
		}

		sort(vi.begin(), vi.end());

		int ret = 0;
		unsigned long long sum = A;
		for (int j = 0; j < N;)
		{
			if (sum <= vi[j])
			{
				int k = 0;
				while (sum <= vi[j] && sum != 1)
				{
					sum += sum - 1;
					++k;
				}

				if ((N-j) <= k || sum == 1) // no need to go further, remove all left
				{
					ret += N-j;
					break;
				}
				else
				{ // continue add
					ret += k;
				}
			}
			else
			{ // absorb
				sum += vi[j];
				++j;
			}
		}

		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}

	return 0;
}