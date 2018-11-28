#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long ll;

int main()
{
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t)
	{
		string S;
		cin >> S;
		vector<int> P(S.size(), -1);
		for(int s=0; s<S.size(); ++s)
		{
			if(S[s] == '+')
			{
				P[s] = 1;
			}
			else
			{
				P[s] = 0;
			}
		}
		ll res = 0;
		if(P.size() == 1)
		{
			if(P[0] == 0)
			{
				res++;
			}
		}
		else
		{
			bool changed;
			do
			{
				changed = false;
				for(int p=0; p<P.size()-1; ++p)
				{
					P[p] = 1-P[p];
					if(P[p] == P[p+1])
					{
						changed = true;
						break;
					}
				}
				if(!changed && P[0] == 0)
				{
					break;
				}
				res++;
			}while(changed);
		}
		cout << "Case #" << t << ": " << res << "\n";
	}
	return 0;
}