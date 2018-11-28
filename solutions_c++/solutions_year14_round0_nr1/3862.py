#include <iostream>
#include <vector>
#include <set>
#include <fstream>

using namespace std;



int main(){
	ofstream output("A-small-attempt2.out");
   ifstream input("A-small-attempt2.in");
	int n;
	input>>n;
	for (int z = 0; z < n; z++)
	{
		int row1, row2;
	vector<vector<int> > matrix1(4,vector<int>(4,0));
	vector<vector<int> > matrix2(4,vector<int>(4,0));

	input>>row1;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
		{
			int tmp;
			input>>tmp;
			matrix1[i][j] = tmp;
		}
	input>>row2;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
		{
			int tmp;
			input>>tmp;
			matrix2[i][j] = tmp;
		}
	set<int> dict1;
	for (int i = 0; i < 4; i++)
		dict1.insert(matrix1[row1-1][i]);
	
	int count = 0;
	int result = 0;
	for (int i = 0; i < 4; i++)
	{
		if (dict1.find(matrix2[row2-1][i]) != dict1.end())
		{
			count++;
			result = *dict1.find(matrix2[row2-1][i]);
		}
	}
	
	if (count == 0) output<<"Case #"<<z+1<<": Volunteer cheated!"<<endl;
	else if (count == 1) output<<"Case #"<<z+1<<": "<<result<<endl;
	else output<<"Case #"<<z+1<<": Bad magician!"<<endl;
	}
	return 0;
}