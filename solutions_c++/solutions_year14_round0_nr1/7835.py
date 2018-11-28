#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	char* inputFile = "A-small-attempt1.in";
	char* ouptFile = "output.txt";
	ifstream input(inputFile);
	ofstream cout(ouptFile);
	int caseNum, opt1, opt2, t, count, result;
	vector<int> tmp;
	input >> caseNum;
	
	for(int i = 0; i < caseNum; i++)
	{
		count = 0;
		tmp.clear();
		
		input >> opt1;
		for(int k = 0; k < 16; k++)
		{
			input >> t;
			if(k >= 4 * (opt1 - 1) && k < 4 * opt1)
			{
				tmp.push_back(t);
			}
		}
		input >> opt2;
		for(int k = 0; k < 16; k++)
		{
			input >> t;
			if(k >= 4 * (opt2 - 1) && k < 4 * opt2 && find(tmp.begin(), tmp.end(), t) != tmp.end())
			{
				result = t;
				count++;
			}
		}
		if(count == 0)
		{
			cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
		}else if(count == 1){
			cout << "Case #" << i + 1 << ": " << result << endl;
		}else{
			cout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
		}
	}
	return 0;
}
