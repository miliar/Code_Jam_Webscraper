#include <iostream> 
#include <vector> 
#include <string> 
#include <algorithm> 
#include <sstream> 
#include <set> 
#include <map> 
#include <queue> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <bitset> 
#include <unordered_map> 
#include <unordered_set> 

using namespace std;
typedef long long ll;





int main(){
#ifdef _CONSOLE 
	freopen("B-small-attempt0 (2).in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		

		int n, k;
		cin >> n>>k;
		vector<double> v(n);
		for (int i = 0; i < v.size(); ++i)
		{
			cin >> v[i];
		}
		vector<int> perm(n, 0);
		for (int i = 0; i < k; ++i)
		{
			perm[i] = 1;
		}
		sort(perm.begin(), perm.end());
		double mxprob = 0;
		do
		{
			vector<double> probs;
			for (int i = 0; i < perm.size(); ++i)
			{
				if (perm[i])
					probs.push_back(v[i]);
			}
			double prob = 0;
			for (int i = 0; i < (1 << k); ++i)
			{
				double tmp = 1;
				int cnt = 0;
				for (int j = 0; j < k; ++j)
				{
					if (i & (1 << j))
					{
						cnt++;
						tmp *= probs[j];
					}
					else
					{
						cnt--;
						tmp *= (1 - probs[j]);
					}
				}
				if (cnt == 0)
					prob += tmp;
			}
			mxprob = max(mxprob, prob);
			

		} while (next_permutation(perm.begin(), perm.end()));
		



		cout << "Case #" << t << ": ";
		printf("%.7lf\n", mxprob);
		
		//cout << "Case #" << t << ": IMPOSSIBLE\n";
	}
	

	return 0;
}

