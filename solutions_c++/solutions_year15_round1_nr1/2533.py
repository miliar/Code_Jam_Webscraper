#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
class Solution{
public:

	int Solve(vector<int> store, int N){

		int sum = 0,tem;
		for (int i = 0; i < N-1; i++)
		{
			tem= store[i]-store[i+1];
			if (tem >= 0)
				sum += tem;
			
		}
		return sum;
	}
	int Solve2(vector<int> store, int N)
	{
		int max = 0,sum=0;
		for (int i = 0; i < N - 1; i++)
		{
			if (max < store[i] - store[i + 1])
				max = store[i] - store[i + 1];
		}
		for (int i = 0; i < N - 1; i++)
		{
			if (store[i] < max)
				sum += store[i];
			else sum += max;
		}
		return sum;
	}
};
void main()
{
	ifstream input("A-large.in");
	ofstream output("output.txt");
	int casenum, B,N;
	int X;
	string finalX = "";
	input >> casenum;
	cout << casenum;
	for (int i = 0; i < casenum; i++)
	{
		input >> N;
		Solution sol;
		vector<int> store;
		for (int i = 0; i < N; i++)
		{
			int tem;
			input >> tem;
			store.push_back(tem);
		}	
		output << "Case #" << i + 1 << ": " << sol.Solve(store,N)<<" "<<sol.Solve2(store,N) << endl;
		cout << i << endl;
	}

}