#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <fstream>
#include <iomanip>
using namespace std;

/*int questionA()
{
	fstream fin("A.in");
	fstream fout("O.txt");
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int N;
		cin >> N;
		string Strings[100];
		for (int j = 0; j < N; j++)
			cin >> Strings[j];
		std::sort(begin(Strings), Strings + N);
		for (int j = 0; j < 100; j++)
		{

	}
	return 0;
}*/

int questionB()
{
	fstream fin("A.in");
	fstream fout("O.txt");
	int T;
	fin >> T;
	for (int i = 1; i <= T; i++)
	{
		int A,B,K;
		fin >> A >> B >> K;
		int count = 0;
		for (int j = 0; j < A; j++)
			for (int k = 0; k < B; k++)
				if ((j & k) < K)
					count++;
		fout << "Case #" << i << ": " << count << endl;
	}
	return 0;
}