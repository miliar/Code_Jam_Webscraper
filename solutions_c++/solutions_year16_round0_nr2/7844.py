#define _SCL_SECURE_NO_WARNINGS
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <ctime>
#include <cmath>
#include <map>
//#include <unordered_map>
#include <list>
#include <set>
#include <random>
#include <stack>
#include <sstream>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;



stack <time_t> time_stack;
void startTimer()
{
	time_stack.push(clock());
}
double stopTimer()
{
	double time = clock() - time_stack.top();
	time_stack.pop();
	return time / double(CLOCKS_PER_SEC);
}



#define MAXN 1000
#define MAXM 500
#define MAXK 100
#define INF int(2e9)
#define MOD 1000000009
#define EPS double(1e-15)
#define LAM double(1e-6)
#define PI double(3.14159265359)


int len = 6;
string gen(int n)
{
	string res;
	for (int i = 0; i < len; i++)
	{
		res = res + (n % 2 == 0 ? '-' : '+');
		n /= 2;
	}
	return res;
}



int main()
{
	startTimer();
	ios::sync_with_stdio(false);
#ifdef _HOME_
	ifstream cin("input.txt");
	ofstream out("output.txt");
	//ofstream cout("output.txt");
	//freopen("output.txt", "w", stdout);
#else
	string TASK = "intersec4";
	//ifstream cin(TASK + ".in");
	//ofstream cout(TASK + ".out");
	//freopen("dfsongrid.out", "w", stdout);
#endif
	cout.precision(9); cout << fixed;


	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		out << "Case #" << t + 1 << ": ";

		string s;
		cin >> s;
		//string s0 = gen(t); s = s0;

		int ans = 0;
		for (int i = s.size() - 1; i >= 0; i--)
			if (s[i] == '-')
			{
				int j;
				for (j = 0; j < i && s[j] == '+'; j++)
					s[j] = '-';
				if (j > 0)
					ans++;

				for (int j = 0; j <= i; j++)
					s[j] = s[j] == '-' ? '+' : '-';
				for (int j = 0; j < (i + 1) / 2; j++)
					swap(s[j], s[i - j]);
				ans++;
			}

		//out << s0 << " ";
		out << ans << endl;
	}


	cout << endl;
#ifdef _HOME_
	cout.precision(3);
	cout << fixed << stopTimer() << "s\n";
	system("pause");
#endif

	return 0;
}