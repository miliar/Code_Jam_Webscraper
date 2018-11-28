#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

typedef set<long long>::iterator ITR;
const long long MAXN = 1e4 + 12 ;
const int MAX_SZ = 5;
set <long long> pal_set;
vector <long long> vec;

long long str2int(string s)
{
	long long result = 0;
	for(int i=0; i<s.size(); i++)
			(result *= 10) += (s[i] - '0');
	return result;
}

void pal(string s)
{
	//cerr << s.size() << endl;
	long long val = str2int(s);
	if (val > MAXN || s.size() > MAX_SZ)
			return;
	if (s[0] != '0') pal_set.insert(val);
	for(char i='0'; i<='9'; i++)
		pal(i + s + i);
	return;
}


int main()
{
	freopen("1.txt", "r", stdin);
	freopen("1_out.txt", "w", stdout);
	pal("1");
	pal("2");
	pal("3");
	pal("4");
	pal("5");
	pal("6");
	pal("7");
	pal("8");
	pal("9");
	pal("");
	for(ITR i = pal_set.begin(); i != pal_set.end(); i++)
	{
		long long val = *i * *i;
		if (val > MAXN || val < 0) break;
		if (pal_set.find(val) != pal_set.end()) vec.push_back(val) ;
	}
//cerr << bool( pal_set.find(100) != pal_set.end()) << endl;
	int n;
	cin >> n;
	for(int i=0; i<n; i++)
	{
		int a, b;
		cin >> a >> b;
		cout << "Case #" << i+1 << ": " << upper_bound(vec.begin(), vec.end(), b) - lower_bound(vec.begin(), vec.end(), a) << endl;
	}
	return 0;

}
