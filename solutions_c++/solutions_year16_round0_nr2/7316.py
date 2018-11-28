#include<iostream>
#include<fstream>

using namespace std;

int count_flips(string s)
{
	int n = s.length();

	int i;

	int count = 0; // flips

	for(i = 0; i < n-1; i++)
	{
		if(s[i] != s[i+1])
			count += 1;
	}

	if(s[n-1] == '-')
		count += 1;

	return count;
}

void test_cases(int t)
{
	int i;

	string input;

	ofstream file;
	file.open("output2");

	for(i = 1;i <= t; i++)
	{
		cin >> input;

		file << "Case #" << i << ": " << count_flips(input) << endl;
	}
}

int main()
{
	int T;
	cin >> T;

	test_cases(T);

	return 0;
}
