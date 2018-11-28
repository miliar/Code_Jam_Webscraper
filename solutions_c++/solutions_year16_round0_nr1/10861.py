// #define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>

// #include <algorithm>
// #include <string>
// #include <cstdio>
// 

//#include <ctime>
//#include <sstream>

using namespace std;

#define TASK "boom1"

/*
for (int intA = 0; intA < v.size(); intA++)
{
	cout << v[intA];
}
cout << "\n";
*/

vector<char> jam;

bool testjam(vector<char> v)
{
	std::sort(v.begin(), v.end());
	int uniqueCount = std::unique(v.begin(), v.end()) - v.begin();
	if (uniqueCount == 10)
		return true;
	else 
		return false;
};

void add_currentnuber_in_vector(int a)
{
	std::string s = std::to_string(a);
	for (int intA = 0; intA < s.size(); intA++)
		jam.push_back(s[intA]);
};


int main()
{
	freopen(TASK ".in", "r", stdin);
	freopen(TASK ".out", "w", stdout);

	ios_base::sync_with_stdio(false);

	int t; // kolvo_testovih_zadac;
	int n; // investigated number;
	int current; // current number;
	int j; // shag;
	int result; // resultat;


	cin >> t;

	

	for (int i = 0; i < t; i++)
	{
		jam.clear();
		jam.resize(0);
		result = 0;
		cin >> n;
		for (int j = 1; j < 1000; j++)
		{
			current = n * j;		
			add_currentnuber_in_vector(current);		
			if (testjam(jam) == true)
			{
				result = j * n;
				cout << "Case #" << i + 1 << ": " << result << "\n";
				j = 1000;
			}
			if (j == 999)
				cout << "Case #" << i + 1 << ": " << "INSOMNIA" << "\n";
		}
	}

	return 0;

}