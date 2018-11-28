#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <stdio.h>
#include <cstdlib>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

struct node
{

};

class TestClass
{

public:
	int numCases;
	fstream fin;

	int A, B, K;

	TestClass()
	{
		numCases = 0;
		fin.open("data.txt", ios::in);
		fin >> numCases;
		fin.get();
	}

	void loadData()
	{
		fin >> A >> B >> K;
	}

	int runtest()
	{
		int count = 0;
		
		for (int i = 0; i < A; i++)
		{
			for (int j = 0; j < B; j++)
			{
				int and = i&j;
				
				//cout << i << " " << j << " " << and << endl;
				

				if (and < K)
				{

					count++;
					//cout << count << endl;
				}

				//system("pause");
			}
		}


		return count;
	}

	int getCases()
	{
		return numCases;
	}

	void reset()
	{

	}
};

int main()
{
	TestClass testClass;

	fstream fout;
	fout.open("dataout.txt", ios::out);

	for (int i = 0; i < testClass.getCases(); i++)
	{
		testClass.loadData();

		fout << "Case #" << i + 1 << ": ";
		

		fout << testClass.runtest() << endl;

		testClass.reset();
	}
	return 0;
}