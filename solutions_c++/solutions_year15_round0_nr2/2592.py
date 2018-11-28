#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
class Solution{
public:
	int num;
	vector<int> store;
	int Solve(vector<int> store){
		sort(store.begin(), store.end());
		if (store[store.size() - 1] <= 3)
			return store[store.size() - 1];
		else
		{
			vector <int> ans;
			int maximum = store[store.size() - 1];
			ans.push_back(maximum);

			vector<int> newvec = store;
			for (int i = 2; i <= maximum / 2; i++)
			{
				vector<int> newvec = store;
				newvec.push_back(i);
				newvec[store.size() - 1] = maximum - i;
				ans.push_back(Solve(newvec) + 1);
			}
			sort(ans.begin(),ans.end());
			return ans[0];
			

		}
	}
};
void main()
{
	ifstream input("B-small-attempt9.in");
	ofstream output("output.txt");
	int casenum, Snum;

	input >> casenum;
	cout << casenum;
	for (int i = 0; i < casenum; i++)
	{
		input >> Snum;
		vector<int> tem;
		for (int j = 0; j < Snum; j++)
		{
			int temint;
			input >> temint;
			tem.push_back(temint);
		}
		Solution sol;
		output << "Case #" << i + 1 << ": " << sol.Solve(tem) << endl;
		cout << i << endl;
	}

}