//#pragma comment(linker, "/STACK:16777216")
#define _CRT_SECURE_NO_WARNINGS

#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <ctime>
#include <memory.h>
#include <assert.h>

#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
#define norm asdfasdgasdgsd

#define eps 1e-9
#define M_PI 3.141592653589793
#define bs 1000000007
#define bsize 256

using namespace std;

const int N = 300031;

int pr[1000];
vector<int> primes;
set<string> done;
int ts, tests, need;
int found_val;
int n;

string get_rand(int len)
{
	string res;
	for (int i = 0; i < len - 2; i++)
	{
		char c = rand() % 2 + '0';
		res += c;
	}
	res = "1" + res + "1";
	return res;
}

int eval(string s, int mod, int base)
{
	int res = 0;
	for (int i = 0; i < s.size(); i++)
	{
		res = res*base;
		res += (s[i] - '0');
		res %= mod;
	}
	return res;
}

int main(){
	//freopen("fabro.in","r",stdin);
	//freopen("fabro.out","w",stdout);
	freopen("F:/in.txt", "r", stdin);
	freopen("F:/output.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	//cin.tie(0);

	pr[1] = 1;
	for (int i = 2; i <= 100; i++)
	{
		if (pr[i] == 0)
		{
			for (int j = i * 2; j <= 100; j += i)
				pr[j] = 1;
		}
	}
	for (int i = 2; i <= 100; i++)
	{
		if (pr[i] == 0)
			primes.push_back(i);
	}

	cin >> tests;
	for (; tests; --tests)
	{
		++ts;
		cout << "Case #" << ts << ":"<<endl;
		cin >> n >> need;
		while (true)
		{
			if (need == 0)
				break;
			string temp = get_rand(n);
			if (done.find(temp) != done.end())
				continue;
			done.insert(temp);
			vector<int> found_vec;
			bool shit = 0;
			for (int i = 2; i <= 10; i++)
			{
				bool found = 0;
				for (int j = 0; j < primes.size(); j++)
				{
					if (eval(temp, primes[j], i) == 0)
					{
						found = 1;
						found_val = primes[j];
					}
				}
				if (found == 0)
					shit = 1;
				found_vec.push_back(found_val);
			}

			if (shit == 0)
			{
				--need;
				cout << temp;
				cerr << temp << "  " << need << endl;
				for (int i = 2; i <= 10; i++)
				{
					cout << " " << found_vec[i - 2];
				}
				cout << endl;
			}
		}
	}

	cin.get(); cin.get();
	return 0;
}