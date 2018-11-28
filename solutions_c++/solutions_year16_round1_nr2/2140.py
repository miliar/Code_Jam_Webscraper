#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>

using namespace std;

vector<int> vv[110];
vector<int> res;
vector<int> tmpv;
vector<bool> tmpf;

int mat[55][55];

bool sortfunc(vector<int> a, vector<int> b)
{
	int len = a.size();
	for(int i = 0; i < len; i++)
	{
		if(a[i] < b[i])
			return true;
		if(a[i] > b[i])
			return false;
	}
	return true;
}

int main()
{
	//freopen("B-small-attempt1.in", "rt", stdin);
	//freopen("test.in", "rt", stdin);
	freopen("B-large.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	int inp, kase, i, j, k, n, tmp;
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		res.clear();
		scanf("%d", &n);
		for(i = 0; i < 2 * n - 1; i++)
		{
			vv[i].clear();
			for(j = 0; j < n; j++)
			{
				scanf("%d", &tmp);
				vv[i].push_back(tmp);
			}
		}
		fprintf(stderr, "Read Input, sorting\n");
		sort(vv, vv + (2 * n - 1), sortfunc);
		fprintf(stderr, "Sorted\n");
		k = -1;
		int kr = -1;
		j = 0;
		for(i = 0; i < n; i++)
		{
			tmpv.clear();
			tmpf.clear();
			for( j = 0; j < 2*n - 1; j++)
			{
				tmpv.push_back(vv[j][i]);
				tmpf.push_back(false);
			}
			sort(tmpv.begin(), tmpv.end());

			if(i == n - 1)
			{
				break;
			}

			if(tmpv[i * 2] != tmpv[i * 2 + 1])
				break;
		}
		k = i;
		int kv = tmpv[i * 2];

		for(i = 0; i < 2 * n -1; i++)
		{
			if(vv[i][k] == kv)
			{
				kr = i;
				break;
			}
		}
		res.push_back(kv);
		for(i = 0; i < n; i++)
		{
			for(j = 0; j < tmpv.size(); j++)
			{
				if(tmpf[j] == true)
					continue;
				if(tmpv[j] == vv[kr][i])
				{
					tmpf[j] = true;
					break;
				}
			}
		}
		for(i = 0; i < tmpv.size(); i++)
		{
			if(tmpf[i] == false)
			{
				res.push_back(tmpv[i]);
			}

		}
		sort(res.begin(), res.end());
		printf("Case #%d:", kase);
		for(j = 0; j < n; j++)
		{
			printf(" %d", res[j]);
		}
		printf("\n");
	}
	return 0;
}