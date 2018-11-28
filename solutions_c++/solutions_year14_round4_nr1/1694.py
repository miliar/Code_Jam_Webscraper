#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

#define SZ 10005

int data[SZ];
bool used[SZ];


int main()
{
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("A-small-attempt0.out", "wt", stdout);


	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int inp, kase, i, j, k, a, n;
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d", &n, &k);
		for(i = 0; i < n; i++)
		{
			scanf("%d", &data[i]);
		}
		sort(data, data + n);
		reverse(data, data + n);

		int pkd = n;
	
		vector<int> tk;
		vector<int> lft;
		vector<int> tall;
		tall.clear();
		tk.clear();

		for(i = 0; i < n; i++)
		{
			tall.push_back(data[i]);
		}

		
		vector<int> tmp;
		while(pkd > 0)
		{
			lft.clear();
			int tn = tall.size();
			for(i = 0; i <= (tn - 1) / 2; i++)
			{
				tk.push_back(tall[i]);
				tk[tk.size() - 1] = k - tk[tk.size() - 1];
				pkd--;
			}
			for(;i < tn; i++)
			{
				lft.push_back(tall[i]);
			}
			sort(tk.rbegin(), tk.rend());
			int cc = 0;
			
			tmp.clear();
			for(i = 0; i < lft.size(); i++)
			{
				if(tk[cc] >= lft[i])
				{
					pkd--;
					tk[cc] = 0;
					cc++;
				}
				else
				{
					tmp.push_back(lft[i]);
				}
			}
			tall = tmp;
		}
		printf("Case #%d: %d\n", kase, tk.size());

	}

	return 0;
}

