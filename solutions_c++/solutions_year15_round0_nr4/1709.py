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
	string str;
	string Solve(int X, int R, int C){
		if (R*C < X)
			return "RICHARD";
		if ((R*C) % X != 0)
			return "RICHARD";
		if (X >= 7)
			return "RICHARD";
		if (X <= 2)
			return "GABRIEL";
		if (R > C)
		{
			str = Solve(X, C, R);
			return str;
		}
		if (X == 3)
		{
			if (R == 1)
				return "RICHARD";
			else
				return "GABRIEL";
		}
			
		if (X == 4)
		{
			if (R <=2)
				return "RICHARD";
			else 
				return "GABRIEL";
		}
		else
		if (X == 5)
		{
			if (R < 3)
				return "RICHARD";
			if (C >= 5)
				return "GABRIEL";
			else
				return "RICHARD";
		}
		if (R < 5)
			return "RICHARD";
		if (C < 6)
			return "RICHARD";
		return "GABRIEL";

	}
};
void main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");
	int casenum,X,R,C;
	Solution sol;
	sol.Solve(3,4,4);
	input >> casenum;
	for (int i = 0; i < casenum; i++)
	{
		input >> X>>R>>C;
		output << "Case #" << i + 1 << ": " << sol.Solve(X, R, C) << endl;
	}

}