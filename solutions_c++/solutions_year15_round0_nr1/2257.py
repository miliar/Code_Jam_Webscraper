#include <iostream>
#include <fstream>
#include <string>
#pragma warning(disable:4996)
using namespace std;
int shyness[1010];
int NUMBER;
int ANS[100];
void input(FILE* f1)
{
	char c;
	fscanf(f1, "%d", &NUMBER);
	fscanf(f1, "%c", &c);
	for (int i = 0; i <= NUMBER; ++i)
	{
		fscanf(f1, "%c", &c);
		shyness[i] = c - '0';
	}
}
int sum(int n)
{
	int s = 0;
	for (int i = 0; i < n; ++i)
		s += shyness[i];
	return s;
}
int ans(int n)
{
	int answer = 0;
	for (int i = 1; i <= n; ++i)
	{
		if (sum(i) >= i)
			continue;
		int d = i - sum(i);
		answer += d;
		shyness[0] += d;
	}
	return answer;
}
int main()
{
	int n;
	string s;
	ifstream f1;
	f1.open("C:\\Users\\ty\\Desktop\\codejam2015\\A.in");
	f1 >> n;
	for (int i = 0; i < n; ++i)
	{
		int num;
		f1 >> num;
		f1 >> s;
		for (int k = 0; k <= num; ++k)
			shyness[k] = s[k] - '0';
		ANS[i] = ans(num);
	}
	ofstream f;
	f.open("C:\\Users\\ty\\Desktop\\codejam2015\\B.txt");
	for (int i = 0; i < n; ++i)
	{
		f << "case #" << i + 1 << ": " << ANS[i] << endl;
	}
	f.close();
	return 0;
}