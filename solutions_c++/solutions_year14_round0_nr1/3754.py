#include <fstream>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <algorithm>
#include <math.h>
using namespace std;

int main()
{
	ifstream curFile("A-small-attempt1.in");
	vector<string> result;
	int T; // testcases count
	const int MAGIC = 16;
	const int LINE = 4;
	int curLine;
	vector<vector<int> > matrix (LINE , vector<int>(LINE , 0));
	vector<bool> dict;
	vector<int> candidate;
	string ret;
	if(curFile.is_open())
	{
		curFile >> T;
		for(int c = 0 ; c < T ; c++)
		{
			candidate.clear();
			ret.clear();
			dict = vector<bool> (1 + MAGIC , false);
			curFile >> curLine;
			curLine --;
			for(int row = 0 ; row < LINE ; row ++)
			{
				for(int col = 0 ; col < LINE ; col ++)
				{
					curFile >> matrix[row][col];
				}
			}			
			for(int col = 0 ; col < LINE ; col ++)
			{
				dict[matrix[curLine][col]] = true;
			}
			curFile >> curLine;
			curLine --;
			for(int row = 0 ; row < LINE ; row ++)
			{
				for(int col = 0 ; col < LINE ; col ++)
				{
					curFile >> matrix[row][col];
				}
			}
			for(int col = 0 ; col < LINE ; col ++)
			{
				if (dict[matrix[curLine][col]] == true)
				{
					candidate.push_back(matrix[curLine][col]);
				}
			}
			if(candidate.size() == 1)
			{
				int temp = candidate[0];
				while(temp > 0)
				{
					ret.push_back(temp % 10 + '0');
					temp /= 10;
				}			
				reverse(ret.begin() , ret.end());	
			}
			else if(candidate.size() > 1)
			{
				ret = "Bad magician!";
			}
			else	
			{
				ret = "Volunteer cheated!";
			}
			result.push_back(ret);
		}	
	}
	curFile.close();
	ofstream outfile;
	outfile.open("result.txt");
	if(outfile.is_open())
	{
		for(int i = 0; i < result.size() ; i++)
			outfile << "Case #" << i + 1<< ": " <<result[i] << endl;
	}
	outfile.close();
	return 0;
}
