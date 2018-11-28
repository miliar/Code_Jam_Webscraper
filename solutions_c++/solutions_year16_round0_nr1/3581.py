#include <iostream>
#include <unordered_set>
#include <vector>
#include <fstream>

using namespace std;

class Solution
{
public:
	void getSolution(vector<int> &cases)
	{

		for (int i = 0; i < cases.size(); ++i)
		{
			int res = valid(cases[i]);
			if (res != -1)
				cout << "Case #" << i + 1 << ": " << res << endl;
			else
				cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
		}
	}

	int valid(int n)
	{
		if (n == 0) return -1;
		unordered_set<int> numSet = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
		int k = 1;
		int m = n;
		while (true)
		{
			int p = n;
			while (p)
			{
				int tmp = p % 10;
				if (numSet.find(tmp) != numSet.end())
					numSet.erase(tmp);
				if (numSet.empty())
					return n;
				p /= 10;
			}
			n = m * (++k);
		}
		return -1;
	}
};

int main()
{
	//freopen("C:/Users/ywy/Desktop/large.in", "r", stdin);
	//freopen("C:/Users/ywy/Desktop/large-out.txt", "w", stdout);
	//freopen("C:/Users/ywy/Desktop/in.in", "r", stdin);
	//freopen("C:/Users/ywy/Desktop/out.txt", "w", stdout);
	int n;
	cin >> n;
	vector<int> vec(n);
	for (int i = 0; i < n; ++i)
	{
		int idata;
		cin >> idata;
		vec[i] = idata;
	}
	Solution ss;
	ss.getSolution(vec);
	return 0;
}