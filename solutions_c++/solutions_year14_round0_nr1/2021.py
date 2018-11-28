#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int getCard (vector<int>& row1, vector<int>& row2, int casenum)	{

	int find = 0;
	for ( int i = 0; i < 4; ++i)	{
		for ( int j = 0; j < 4; ++j)	{
			if (row1[i] == row2[j])	{
				if (find == 0)
					find = row1[i];
				else return -1;
			}
		}
	}
	return find;

}

int main()	{

	int N = 0;
	int testcase = 0;
	string str;
	getline(cin, str);
	stringstream(str) >> testcase;
	vector< vector<int> > matrix(testcase*8, vector<int>());
	vector<int> ans;
	int line = 0;
	while (getline(cin, str))
	{
		stringstream sst(str);
		if (line%5 == 0) {
			sst>>N;
			ans.push_back(N);
		}
		else
			while (sst.good())	{
				sst>>N;
				matrix[line - ans.size()].push_back(N);
			}
		line++;
	}

	for ( int i = 0; i < testcase; ++i)	{
		cout<<"Case #"<<i+1<<": ";
		int card = getCard(matrix[i*8 + ans[i*2]-1], matrix[i*8+4 + ans[i*2+1]-1], i);
		if ( card >=1 && card <= 16 ) cout<<card<<endl;
		else if (card == -1)	cout<<"Bad magician!"<<endl;
		else cout<<"Volunteer cheated!"<<endl;
	}

	return 0;
}