#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>

using namespace std;

char abc[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

bool checkcond(vector<int> v, int total)
{
	int maxel = *max_element(v.begin(), v.end());
	return (maxel <= total / 2);		
}

void testcase()
{
	int n;
	cin >> n;
	vector< int> ps(n);
	vector< int> ind(n);
	int total = 0;
	for (int i = 0; i < n; ++i)
	{
		cin >> ps[i];
		total += ps[i];
		ind[i] = i;
	}

	while (total > 0)
	{
		int num = max_element(ps.begin(), ps.end()) - ps.begin();

		if (ps[num] >= 2)
		{
			ps[num] -= 2;
			total -= 2;
			if (!checkcond(ps, total))
			{
				ps[num]++;
				total++;
				
				int mx = -100;
				int num1 = -1;
				for(int i = 0; i < ps.size(); ++i)
				{ 
					if (num != i && (num1 == -1 || mx < ps[i]))
					{
						num1 = i;
						mx = ps[i];
					}
				}

				ps[num1]--;
				total--;

				if (!checkcond(ps, total))
				{
					ps[num1]++;
					total++;

					cout << abc[num] << " ";
				}
				else
				{
					cout << abc[num] << abc[num1] << " ";
				}
			}
			else
				cout << abc[num] << abc[num] << " ";
		}
		else
		{
			ps[num] --;
			total --;
			int mx = -100;
			int num1 = -1;
			for (int i = 0; i < ps.size(); ++i)
			{
				if (num != i && (num1 == -1 || mx < ps[i]))
				{
					num1 = i;
					mx = ps[i];
				}
			}

			ps[num1]--;
			total--;

			if (!checkcond(ps, total))
			{
				ps[num1]++;
				total++;

				cout << abc[num] << " ";
			}
			else
			{
				cout << abc[num] << abc[num1] << " ";
			}
		}
	}
	cout << endl;
} 

int main()
{
  int n;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
    cout << "Case #" << i + 1 << ": ";
		testcase();
	}
	
	return 0;
}