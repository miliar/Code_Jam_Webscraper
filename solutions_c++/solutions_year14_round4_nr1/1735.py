#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<bitset>
#include<map>
#include<set>
using namespace std;



int main()
{

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int tt;
	cin >> tt;
	for(int t = 1; t <= tt; t++)
	{
		int m;
		int n;
		cin >> n >> m;
		multiset<int> ss, ss2;
		vector<int> f(n);
		vector<int> ff(n);
		for(int i  =0; i < n; i++)
		{
			ff[i] = 0;
			cin >> f[i];
			ss2.insert(m-f[i]);
			ss.insert(f[i]);
			
		}
		sort(f.begin(), f.end());
		reverse(f.begin(), f.end());
		int end = n-1;
		int res = 0;

		//for(multiset<int>::iterator it = ss.begin(); it != ss.end(); it++)
		//{
		//	multiset<int>::iterator it2 = ss2.lower_bound(m - *it);
		//	if(it)
		//}

		for(int i = 0; i  <n; i++)
		{
			if(ff[i] == 0)
			{
				for(int j = i+1; j <n; j++ )
				{
					if(ff[j] == 0)
					{
						if(f[i]+f[j]<=m)
						{
							ff[j] = 1;
							break;
						}
					}
				}
				res++;
			}
			
		}

		/*		for(int i = 0; i <= end; i++)
{
			if(f[i] + f[end] <= m)
			{
				res++;
				end--;
			}
			else
			{
				res++;
			}
		}*/

		printf("Case #%d: %d\n", t, res);


    }
	return 0;
}