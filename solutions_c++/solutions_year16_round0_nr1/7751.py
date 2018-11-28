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

		ll n; cin >> n;

		if (n == 0)
			out << "INSOMNIA";
		else
		{
			set <int> st;
			ll i;
			for (i = 1; st.size() < 10; i++)
			{
				ll m = i*n;
				while (m > 0)
				{
					st.insert(m % 10);
					m /= 10;
				}
			}

			out << (i - 1)*n;
		}

		out << endl;
	}


	cout << endl;
#ifdef _HOME_
	cout.precision(3);
	cout << fixed << stopTimer() << "s\n";
	system("pause");
#endif

	return 0;
}