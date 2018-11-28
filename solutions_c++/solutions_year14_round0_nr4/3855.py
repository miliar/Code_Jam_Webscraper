#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen ("outputjam.txt","w",stdout);
	int r,c,m;
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int n;
		cin >> n;
		vector<double> na(n),ke(n);
		for (int i = 0; i < n; i++)
			cin >> na[i];
		for (int i = 0; i < n; i++)
			cin >> ke[i];
		sort (na.begin(),na.end());
		sort (ke.begin(),ke.end());

		vector<bool> mr(n);
		int war = 0;
		for (int i = 0; i < na.size(); i++)
		{
			int id = -1;
			for (int j = 0; j < ke.size(); j++)
			{
				if (na[i] < ke[j] && !mr[j])
				{
					id = j;
					mr[j] = true;
					break;
				}
			}
			if (id == -1)
				war++;
		}
		int dicwar = 0;
		fill(mr.begin(),mr.end(),false);
		for (int i = 0; i < na.size(); i++)
		{
			int id = -1;
			for (int j = 0; j < ke.size(); j++)
			{
				if (na[i] > ke[j] && !mr[j])
				{
					dicwar++;
					id = j;
					mr[j] = true;
					break;
				}
			}
			//if (id == -1)
			//	dicwar++;
		}
		printf ("Case #%d: %d %d\n",i + 1,dicwar,war);
	}

	return 0;
}