#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int k=1; k<=T; k++)
	{
		vector<double> naomi, ken;
		vector<double>().swap(naomi);
		vector<double>().swap(ken);
		int N;
		double temp;
		cin >> N;
		for (int i=0; i<N; i++)
		{
			cin >> temp;
			naomi.push_back(temp);
		}
		for (int i=0; i<N; i++)
		{
			cin >> temp;
			ken.push_back(temp);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int res1 = 0, p=0, q=0;
		while (p<N && q<N)
		{
			if (naomi[p] > ken[q])
			{
				res1++;
				p++;
				q++;
			}
			else
				p++;
		}
		int res2 = 0;
		p=0, q=0;
		while (p<N && q<N)
		{
			if (ken[q] > naomi[p])
			{
				res2++;
				p++;
				q++;
			}
			else
				q++;
		}
		cout << "Case #" << k << ": " << res1 << " " << N-res2 << endl;
	}
	return 0;
}