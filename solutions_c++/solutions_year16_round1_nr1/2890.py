#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>
#include <list>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (n); ++i)
#define SIZEOF(a) (sizeof(a)/sizeof((a)[0]))

typedef long long ll;

void SolveCase()
{
	string s; cin >> s;
	const size_t n = s.size();
	list<char> res;
	FOR(i,n){
		if(i==0)
		{
			res.push_back(s[i]);
		}
		else
		if(s[i] >= res.front())
		{
			res.push_front(s[i]);
		}
		else
		{
			res.push_back(s[i]);
		}
	}
	for(auto it = res.begin(); it != res.end(); ++it){
		cout << *it;
	}
}

void test()
{
}

int main()
{
	//test();return 0;
	int t; cin >> t;
	FOR(i,t){
		cout << "Case #" << i+1 << ": ";
		SolveCase();
		cout << endl;
	}
	return 0;
}