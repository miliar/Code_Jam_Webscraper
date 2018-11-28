#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <string>
#include <map>
#include <math.h>
#include <iomanip>
#include <assert.h>
using namespace std;
//
//char winner(char c1, char c2)
//{
//	if (c1 > c2) swap(c1, c2);
//	if (c1 == 'P')
//	{
//		if (c2 == 'S') return c2;		
//	}
//	return c1;
//}
//
//bool check(vector<char> mas)
//{
//	while (mas.size() > 1)
//	{
//		vector<char> tmp(mas.size() / 2);
//		bool b = false;
//		for (int i = 0; i < mas.size()/2; ++i)
//		{
//			if (mas[i * 2] == mas[i * 2 + 1])
//			{
//				b = true;
//				break;
//			}
//			tmp[i] = winner(mas[i * 2], mas[i * 2 + 1]);
//		}
//		if (b)
//			break;
//		mas.assign(tmp.begin(), tmp.end());
//	}
//	if (mas.size() == 1)
//		return true;
//	else return false;
//}
int k1;
double res (vector<double> & cands)
{
	int k = cands.size();
	assert(k1 == k);
	vector<vector<double>> votes(k + 1, vector<double>(k/2 + 1));
		votes[0][0] = 1;
		for (int i = 1; i <= k; ++i)
		{
			votes[i][0] = votes[i - 1][0] * (1 - cands[i - 1]);
			for (int j = 1; j < k/2 + 1; ++j)
			{
				votes[i][j] = votes[i - 1][j - 1] * cands[i - 1] + votes[i - 1][j] * (1 - cands[i - 1]);
			}
		}
		return votes[k][k/2];
}

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int T;
	cin>>T;

	for (int i1 = 0; i1 < T; ++i1)
	{
		int n,k;
		cin>>n>>k;
		k1 = k;
		vector<double> probs(n);
		for (int i = 0; i < n; ++i)
			cin>>probs[i];
		sort(probs.begin(), probs.end());
		vector<double> cands(k);
		for (int i = 0; i < k/2; ++i)
		{
			cands[k - i - 1] = probs[n - i - 1];
			cands[i] = probs[i];
		}
		double r = res(cands);
		for (int i = 0; i < n - k + 1; ++i)
		{
			cands.assign(probs.begin() + i, probs.begin() + i + k);
			r = max(r, res(cands));
		}		
		for (int i = 1; i < k; ++i)
		{
			for (int j = 0; j < i; ++j)
				cands[j] = probs[j];
			for (int j = i; j < k; ++j)
				cands[j] = probs[n - k + j];
			r = max(r, res(cands));
		}
		cout<<fixed<<setprecision(8)<<"Case #"<<i1 + 1<<": "<<r<<endl;
	}
	
	return 0;
}