#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ifstream ifs("C-small-attempt0.in");
	ofstream ofs("C.out");
	cin.rdbuf(ifs.rdbuf());
	cout.rdbuf(ofs.rdbuf());
	int t;
	cin >> t;
	long long a, b;
	int i = 0;
	vector<long long> v;
	v.push_back(1);
	v.push_back(4);
	v.push_back(9);
	v.push_back(121);
	v.push_back(484);
	while (t--)
	{
		++i;
		cin >> a >> b;
		sort(v.begin(), v.end());
		int r = v.size();
		int sz = v.size();
		for (int j = 0; j < sz; ++j)
		{
			if (a <= v[j])
			{
				break;
			}
			r--;
		}
		
		for (int j = sz - 1; j >= 0; --j)
		{
			if (b >= v[j])
			{
				break;
			}
			r--;
		}
		
		cout << "Case #" << i << ": " << r << endl; 
	}
	ofs.close();
	ifs.close();
	return 0;
}