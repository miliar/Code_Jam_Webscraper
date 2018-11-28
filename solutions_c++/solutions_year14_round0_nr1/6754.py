#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
void magicTrick();
int main()
{

	int i;
	
	magicTrick();
	
	cin >> i;
	return 0;
}

void magicTrick()
{
	ifstream input("A-small-attempt1.in");
	//ifstream input("input.txt");
	ofstream cout("output.txt");
	int caseNum, opt1, opt2, i, j, k, t, count, result;
	vector<int> tmp;
	input >> caseNum;
	for(i = 0; i < caseNum; i++)
	{
		count = 0;
		tmp.clear();
		input >> opt1;
		for(k = 0; k < 16; k++)
		{
			input >> t;
			if(k >= 4 * (opt1 - 1) && k < 4 * opt1)
			{
				tmp.push_back(t);
				//cout << "tmp " << t;
			}
		}
		input >> opt2;
		//cout << "i " << i << "  opt1=" << opt1 << "  opt2=" << opt2 << endl;
		for(k = 0; k < 16; k++)
		{
			input >> t;
			if(k >= 4 * (opt2 - 1) && k < 4 * opt2)
			{
				//cout << "target " << t; 
				if(find(tmp.begin(), tmp.end(), t) != tmp.end())
				{
					result = t;
					count++;
					//cout << "count" << count ;
				}
			}
		}
		if(count == 0)
			cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
		else if(count == 1)
			cout << "Case #" << i + 1 << ": " << result << endl;
		else
			cout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
	}
}
