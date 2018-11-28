#include<iostream>
#include<cstring>

using namespace std;

string getNum(string s)
{
	int o[26];

	for(int i = 0;i < 26;i++)
		o[i] = 0;

	int res[10];

	for(int i = 0;i < 10;i++)
		res[i] = 0;

	int n = s.length();

	for(int s_i = 0; s_i < n;s_i++)
	{
		o[s[s_i]-'A'] += 1;
	}

	o[14] -= o[25];
	o[17] -= o[25];
	res[0] += o[25];

	o[14] -= o[22];
	res[2] += o[22];

	o[5] -= o[20];
	o[14] -= o[20];
	o[17] -= o[20];
	res[4] += o[20];

	o[18] -= o[23];
	res[6] += o[23];

	res[8] += o[6];

	o[13] -= o[18];
	res[7] += o[18];

	o[13] -= o[14];
	res[1] += o[14];

	res[3] += o[17];

	res[5] += o[5];

	res[9] += o[13]/2;

	string ret = "";

	for(int i = 0;i < 10;i++)
	{
		for(int j = 0;j < res[i];j++)
		{
			ret += to_string(i);
		}
	}

	return ret;
}

void test()
{
	int T;
	cin >> T;

	string s;

	for(int i = 0;i < T;i++)
	{
		cin >> s;

		cout << "Case #" << i+1 << ": " << getNum(s) << "\n";
	}
}

int main()
{
	test();
	return 0;
}
