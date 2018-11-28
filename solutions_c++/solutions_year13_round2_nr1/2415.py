#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;
#define ULL unsigned long long

int main()
{
	ios_base::sync_with_stdio(false);

	vector<ULL> v;
	ULL a, n, t;
	ULL min_changes = 0;

	cin >> t;

	for(ULL j = 1; j <= t; j++)
	{
		cin >> a;
		cin >> n;

		//Read all motes
		while(n)
		{
			ULL tmp; cin >> tmp;
			v.push_back(tmp);
			n--;
		}

		sort(v.begin(), v.end());

		if(a != 1)
		{

			for(ULL i = 0; i < v.size(); i++)
			{
				if(a > v[i])
					a += v[i];
				else //cant absorb
				{
					int tmpSize = a;
					int tmpChanges = 0;
					while(tmpSize <= v[i])
					{
						tmpSize += tmpSize - 1;
						tmpChanges++;
					}

					if(tmpChanges >= v.size() - i )
					{
						min_changes += v.size() - i;
						break;
					}

					min_changes += tmpChanges;
					a = tmpSize;
					i--;
				}
			}
		}
		else
			min_changes = v.size();

		cout << "Case #" << j << ": " << min_changes << '\n';
		v.clear();
		min_changes = 0;

	}

	return 0;
}