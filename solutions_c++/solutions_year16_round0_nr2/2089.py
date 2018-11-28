#include "string.h"
#include <cstring>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <map>
#include <stack>
#include <list>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <limits.h>
#include <fstream>
using namespace std;


/*void countDigitals(vector<int>& digitals, long long n, int& count)
{
	while (n > 0){

		int d = n % 10;
		if (!digitals[d]){
			digitals[d] = 1;
			++count;
		}
		n = n / 10;
	}
}

int main()
{
	int t, n;
	ifstream istream;
	istream.open("input.in");
	istream >> t;
	ofstream ostream;
	ostream.open("output.in");
	int i = 0;
	while (t--)
	{
		i++;
		istream >> n;
		if (n == 0) {
			ostream << "Case #" << i << ": " <<"INSOMNIA" << endl;
			continue;
		}
		vector<int> digitals(10, 0);
		int count = 0;
		long long digital = 0;
		while (count < 10)
		{
			digital += n;
			countDigitals(digitals, digital, count);
		}
		ostream << "Case #" << i << ": " << digital << endl;
	}
	ostream.flush();
	ostream.close();
	return 0;
}*/

int main()
{
	int f[101] = { 0 }; //表示以+为开头的+-+-模式串， f[i]表示长度为i的串需要的最少变换次数
	int g[101] = { 0 }; //表示以-为开头的-+-+模式串

	f[1] = 0; g[1] = 1; g[2] = 1; f[2] = 2;
	for (int i = 3; i <= 100; i++)
	{
		if (i % 2)
		{
			f[i] = 1 + g[i - 1];//表示翻转一次
			g[i] = 1 + f[i];
		}
		else
		{
			f[i] = 2 + f[i - 2];
			g[i] = g[i - 1];
		}
	}
	
	/*for (int i = 1; i <= 100; i++)
	{
		cout << i << " " << f[i] << " " << g[i] << endl;
	}*/

	int t;
	ifstream istream;
	istream.open("input.in");
	istream >> t;
	ofstream ostream;
	ostream.open("output.in");
	int index = 0;
	while (t--)
	{
		index++;
		bool start_add = true;
		string str;
		istream >> str;
		
		int len = str.length();
		start_add = str[0] == '+';
		int count = 1;
		for (int i = 1; i < len; i++)
		{
			if (str[i] != str[i - 1]) count++;
		}
		int value = start_add ? f[count] : g[count];
		ostream << "Case #" << index << ": " << value << endl;
	}
	return 0;
}