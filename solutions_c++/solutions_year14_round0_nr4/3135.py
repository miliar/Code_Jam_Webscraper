#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n;
		cin >> n;
		vector<double> v1(n);
		vector<double> v2(n);
		for (int i = 0; i < n; i++)
			cin >> v1[i];
		for (int i = 0; i < n; i++)
			cin >> v2[i];
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());

		int numOne = 0;
		int index1 = 0;
		for (int i = 0; i < n; i++)
		{
			while (index1 < n && v2[index1] < v1[i])
			{
				index1++;
			}
			if (index1 < n)
			{
				numOne++;
				index1++;
			}
		}
		numOne = n - numOne;
		int numTwo = 0;
		index1 = 0;
		for (int i = 0; i < n; i++)
		{
			while (index1 < n && v1[index1] < v2[i])
			{
				index1++;
			}
			if (index1 < n)
			{
				numTwo++;
				index1++;
			}
		}
		cout << numTwo << " " << numOne << endl;
	}
	return 0;
}
