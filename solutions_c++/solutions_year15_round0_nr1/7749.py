#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <math.h>
// #include <numeric>      // std::inner_product
#include <stdlib.h>     /* atoi */

//#include <ctime>
//#include <sstream>

using namespace std;

#define TASK "ovation"

// Standing Ovation



int main()
{
	//	clock_t begin = clock();

	freopen(TASK ".in", "r", stdin);
	freopen(TASK ".out", "w", stdout);

	ios_base::sync_with_stdio(false);

	int T;
	int S;

	cin >> T;

	string line;
	vector<int> lineInt;

	int result;
	int currentStandUp;

	for (int intC = 1; intC < T+1; intC++)
	{

		line.clear();
		line.resize(0);
		lineInt.clear();
		lineInt.resize(0);
		result = 0;
		currentStandUp = 0;

		cin >> S;
//		cout << S << endl;
		
		for (int i = 0; i < S+1; i++)
		{
			char a;
			int b;
		    cin >> a;
//			cout << a << endl;
			b = atoi(&a);
			lineInt.push_back(b);
		}

		for (int i = 0; i < lineInt.size(); i++)
		{
			if (i <= currentStandUp)
				currentStandUp = currentStandUp + lineInt[i];
			else
			{
				result += i - currentStandUp;
				currentStandUp = i + lineInt[i];
			}
		}
		cout << "Case #" << intC << ": "  << result << endl;


	}

	/*
	clock_t end = clock();
	long elapsed_secs = end - begin;
	cout << "time" << elapsed_secs; */
}