// K1
// :)

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <string>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>

#define EPS 1e-8
#define PI 3.141592653589793
#define X first
#define Y second
#define FX(x) fixed << setprecision((x))

using namespace std;

typedef pair<int, int> point;
typedef set<int>::iterator ITR;
const int MAXN = 2e5 + 123;

vector <string> words;
void genarate(string s, string keys, int n)
{
	if(s.size() == n)
	{
		 words.push_back(s);
		 return;
	}
	for (int i = 0; i < keys.size(); ++i)
	{
		genarate(s + keys[i], keys, n);
	}
	return;
}

int mx_pay = -1;

int count2(string source, string target)
{
	int result = 0;
	while(true)
	{
		int pos = source.find(target);
		if(pos == string::npos) break;
		result ++;
		source = source.substr(pos + 1, source.size());
	}
	mx_pay = max(mx_pay, result);
	return result;
}

double wcount(string s)
{
	double result = 0 ;
	long long sum = 0;
	for (int i = 0; i < words.size(); ++i)
		sum += count2(words[i], s);
	cerr << sum << endl;
	result = (double) sum / (double) words.size();
	return result;
}

int main()
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		mx_pay = -1;
		words.clear();
		int k, l, s;
		string keys, target;
		cin >> k >> l >> s;
		cin >> keys >> target;
		genarate("", keys, s);
		cerr << "Generated " << words.size() << endl;
		double result = wcount(target);
		cout << "Case #" << test + 1 << ": " << FX(7) << mx_pay - result << endl;

	}

	return 0;
}