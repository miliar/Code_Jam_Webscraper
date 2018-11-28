#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdlib.h>
using namespace std;

int main()
{
	string line;
	int numtc;
	ifstream myfile ("B-large.in");
//	ifstream myfile ("input.txt");
	getline (myfile,line);
	numtc = atoi(line.c_str());

	int N=0;
	int M=0;
	vector< vector<int> > lawn;
	vector<int> lawnRow;
	vector<int> rowMax;
	vector<int> colMax;

	for(int testCaseNum=1; testCaseNum <= numtc; testCaseNum++)
	{
		lawn.clear();
		rowMax.clear();
		colMax.clear();
		if (myfile.is_open())
		{
			myfile >> N;
			myfile >> M;
			int temp;

			for(int i=0; i<N; i++)
			{
				lawnRow.clear();
				for(int j=0; j<M; j++)
				{
					myfile>>temp;
					lawnRow.push_back(temp);

				}
				lawn.push_back(lawnRow);
			}
		}

		int max;
		for(int i=0; i<N; i++)
		{
			max=0;
			for(int j=0; j<M; j++)
			{
				if(lawn[i][j] > max) max = lawn[i][j];
			}
			rowMax.push_back(max);
		}

		for(int i=0; i<M; i++)
		{
			max=0;
			for(int j=0; j<N; j++)
			{
				if(lawn[j][i] > max) max = lawn[j][i];
			}
			colMax.push_back(max);
		}

		int redflag = 0;
		for(int i=0; i<N; i++)
		{
			for(int j=0; j<M; j++)
			{
				if(lawn[i][j] < rowMax[i] && lawn[i][j] < colMax[j]) redflag = 1;
				if(redflag==1) break;
			}
			if(redflag==1) break;
		}

		if(redflag) cout << "Case #"<< testCaseNum << ": " << "NO" << endl;
		else cout << "Case #"<< testCaseNum << ": " << "YES" << endl;
	}
	myfile.close();
	return 0;
}

