#include<climits>
#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

void war(vector<float> &naomi, vector<float> &ken)
{
	

	sort(naomi.begin(), naomi.end());
	
	sort(ken.begin(), ken.end());

	/*cout << "naomi" << endl;
	for (auto x : naomi)
		cout << x << " ";
	cout << endl;

	cout << "ken" << endl;
	for (auto x : ken)
		cout << x << " ";
	cout << endl;*/


	reverse(naomi.begin(), naomi.end());

	int n = ken.size();

	int z = 0;
	auto nao = 0;
	auto endken = n-1;
	auto beginken = 0;
	
	while ( nao < n && beginken <= endken)
	{
		if (naomi[nao] > ken[beginken] && naomi[nao] > ken[endken])
		{
			z++;
			beginken++;
		}
		else
		{
			endken--;
		}
		nao++;
	}


	
	reverse(naomi.begin(), naomi.end());
	

	int y = 0;
	int nLost = ken.size() - 1;
	int neoLost = 0;
	int kenWinBegin = 0;
	int kenWinend = ken.size() - 1;
	

		while (neoLost <= nLost && kenWinBegin <= kenWinend)
		{
			if (naomi[neoLost] < ken[kenWinBegin])
			{
				kenWinend--;
				neoLost++;
			}
			else
			{
				if (naomi[neoLost] > ken[kenWinBegin])
				{
					y++;
					neoLost++;
					kenWinBegin++;
				}

			}
			    
				
				
			
		}
		
		//cout << "outside while " << y << endl;
		
	
	
	cout << y << " " << z << endl;

	

}

int main()
{
	int T = 0;
	
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int n = 0;
		cin >> n;
		vector<float> naomi;
		vector<float> ken;
		for (int j = 0; j < n; j++)
		{
			float t = 0;
			cin >> t;
			naomi.push_back(t);
		}

		for (int j = 0; j < n; j++)
		{
			float t = 0;
			cin >> t;
			ken.push_back(t);
		}

		cout << "Case #" << i + 1 << ": ";
		war(naomi, ken);
	}

	
}