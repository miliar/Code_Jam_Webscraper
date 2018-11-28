#include <iostream>
#include <vector>

using namespace std;

int main()
{
	//freopen("..\\Debug\\in.txt", "r", stdin);
	
	freopen("..\\Debug\\A-small-attempt0.in", "r", stdin);freopen("..\\Debug\\A-small-attempt0.out", "w", stdout);
	//freopen("..\\Debug\\A-large-practice.in", "r", stdin);freopen("..\\Debug\\A-large-practice.out", "w", stdout);

	const int SIZE = 4;
	int num, mat[SIZE][SIZE], count[SIZE*SIZE+1], answer;
	vector<int> results;
	cin >> num;
	for(int i=0; i<num; i++)
	{
		for(int j=0; j<SIZE*SIZE+1; j++) count[j] = 0;

		cin >> answer;
		for(int j=0; j<SIZE; j++)
		{
			for(int k=0; k<SIZE; k++)
			{
				cin >> mat[j][k];
			}
		}
		for(int j=0; j<SIZE; j++) count[mat[answer-1][j]]++;

		cin >> answer;
		for(int j=0; j<SIZE; j++)
		{
			for(int k=0; k<SIZE; k++)
			{
				cin >> mat[j][k];
			}
		}
		for(int j=0; j<SIZE; j++) count[mat[answer-1][j]]++;

		results.clear();
		for(int j=0; j<SIZE*SIZE+1; j++)
		{
			if(count[j] == 2) results.push_back(j);
		}

		switch(results.size())
		{
		case 0:
			cout << "Case #" << (i+1) << ": Volunteer cheated!" << endl;
			break;
		case 1:
			cout << "Case #" << (i+1) << ": " << results.at(0) << endl;
			break;
		default:
			cout << "Case #" << (i+1) << ": Bad magician!" << endl;
			break;
		}
	}
	return 0;
}