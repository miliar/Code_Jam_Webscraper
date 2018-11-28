#include <iostream>
#include <fstream>
#include <string>
using namespace std;
class Solution{
public:
	int maxS;
	string Sdistribute;
	Solution(int a, string str) :maxS(a), Sdistribute(str)
{}
	int Solve(){
		if (maxS == 0)
			return 0;
		int count=0,now=0;
		for (int i = 0; i <= maxS; i++)
		{
			if (now >= i)
			{
				now += Sdistribute[i]-'0';
			}
			else
			{
				count += i - now;
				now = i+Sdistribute[i]-'0';
			}
		}
		return count;
		
	}
};
void main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");
	int casenum,Snum;
	string str;
	input >> casenum;
	for (int i = 0; i < casenum; i++)
	{
		input >> Snum;
		input >> str;
		Solution sol(Snum, str);
		output <<"Case #"<<i+1<<": "<< sol.Solve() << endl;
	}

}