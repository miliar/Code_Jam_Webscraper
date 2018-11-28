// GCJ.cpp : Defines the entry point for the console application.
//
#include <string>
#include <iostream>
#include <vector>

using namespace std;

void readUserChoice(int &row, vector<int> &mat){
	scanf("%d", &row);
	string line;
	getline(cin, line);
	for(int i = 0; i < 4; ++i)
	{
		int stIdx = 4 * i;
		getline(cin, line);
		sscanf(line.c_str(), "%d %d %d %d", 
			&mat[stIdx], &mat[stIdx + 1], 
			&mat[stIdx + 2], &mat[stIdx + 3]);
	}
}

int sameCount(vector<int> &row1, vector<int> &row2, int &cardNum)
{
	int sameCount = 0;
	for(int i = 0; i < row1.size(); ++i)
	{
		int r1i = row1[i];
		for(int j = 0; j < row2.size(); ++j)
		{
			if(r1i == row2[j]) 
			{
				cardNum = r1i;
				++sameCount;
			}
		}
	}
	return sameCount;
}

void solve_A(){
	int caseNum;
	scanf("%d", &caseNum);
	string line;
	getline(cin, line);

	vector<int> mat(16);
	int row;
	for(int i = 0; i < caseNum; ++i)
	{
		printf("Case #%d: ", i + 1);

		readUserChoice(row, mat);
		vector<int> row1(4);
		vector<int>::iterator iter = mat.begin() + (row - 1) * 4;
		copy(iter, iter + 4, row1.begin()); 

		readUserChoice(row, mat);
		vector<int> row2(4);
		iter = mat.begin() + (row - 1) * 4;
		copy(iter, iter + 4, row2.begin());

		int cardNum = 0;
		int count = sameCount(row1, row2, cardNum);
		if(count == 0)
		{
			printf("Volunteer cheated!");
		}
		else if(count == 1)
		{
			printf("%d", cardNum);
		}
		else
		{
			printf("Bad magician!");
		}

		printf("\n");
	}
}

void readLine_B(const string &line, double &C, double &F, double &X)
{
	sscanf(line.c_str(), "%lf %lf %lf", &C, &F, &X);
}

double bestTime_B(double C, double F, double X)
{
	double leftOver = X;
	double rate = 2.0;
	double time = 0.0;
	while(X/rate > (C/rate + X/(rate + F)))
	{
		time += C/rate;
		rate += F;
	}
	time += X/rate;
	return time;
}

void solve_B(){
	int caseNum;
	scanf("%d", &caseNum);
	string line;
	getline(cin, line);

	double C, F, X;
	for(int i = 0; i < caseNum; ++i)
	{
		getline(cin, line);
		readLine_B(line, C, F, X);
		double time = bestTime_B(C, F, X);
		printf("Case #%d: %.7f\n", i + 1, time);
	}
}

int main()
{
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);

	solve_B();
	return 0;
}



