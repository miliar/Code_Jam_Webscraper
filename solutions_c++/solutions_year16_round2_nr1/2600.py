#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iterator>
#include <stack>
#include <queue>

#define FOR(i,a,n) for(int i = (a); i < (int)(n); ++i)
#define MAX(a,b) ((a) > (b)? (a) : (b))
#define MIN(a,b) ((a) < (b)? (a) : (b))
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int k,c,s,t;
	string ss;
	
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		int a[27] = {0};
		int tmp; 
		vector <int> ar;
		cin >> ss;
		for(int j = 0; j < ss.length(); j++)
			a[ss[j] - 'A']++;
		if(tmp = a['Z' - 'A'])
		{
			FOR(k, 0, a['Z' - 'A'])
				ar.push_back(0);
			a['Z' - 'A'] -= tmp;
			a['E' - 'A'] -= tmp;	
			a['R' - 'A'] -= tmp;
			a['O' - 'A'] -= tmp;	
		}
		if(tmp = a['U' - 'A'])
		{
			FOR(k, 0, a['U' - 'A'])
				ar.push_back(4);
			a['F' - 'A'] -= tmp;	
			a['O' - 'A'] -= tmp;
			a['U' - 'A'] -= tmp;	
			a['R' - 'A'] -= tmp;
		}		
		if(tmp = a['X' - 'A'])
		{
			FOR(k, 0, a['X' - 'A'])
				ar.push_back(6);
			a['S' - 'A'] -= tmp;
			a['I' - 'A'] -= tmp;	
			a['X' - 'A'] -= tmp;
		}
		if(tmp = a['G' - 'A'])
		{
			FOR(k, 0, a['G' - 'A'])
				ar.push_back(8);
			a['E' - 'A'] -= tmp;	
			a['I' - 'A'] -= tmp;	
			a['G' - 'A'] -= tmp;
			a['H' - 'A'] -= tmp;
			a['T' - 'A'] -= tmp;
		}
		if(tmp = a['S' - 'A'])
		{
			FOR(k, 0, a['S' - 'A'])
				ar.push_back(7);
			a['S' - 'A'] -= tmp;	
			a['E' - 'A'] -= tmp;	
			a['V' - 'A'] -= tmp;
			a['E' - 'A'] -= tmp;
			a['N' - 'A'] -= tmp;
		}
		if(tmp = a['R' - 'A'])
		{
			FOR(k, 0, a['R' - 'A'])
				ar.push_back(3);
			a['T' - 'A'] -= tmp;	
			a['H' - 'A'] -= tmp;	
			a['R' - 'A'] -= tmp;
			a['E' - 'A'] -= tmp;
			a['E' - 'A'] -= tmp;
		}
		if(tmp = a['F' - 'A'])
		{
			FOR(k, 0, a['F' - 'A'])
				ar.push_back(5);
			a['F' - 'A'] -= tmp;	
			a['I' - 'A'] -= tmp;	
			a['V' - 'A'] -= tmp;
			a['E' - 'A'] -= tmp;
		}
		if(tmp = a['I' - 'A'])
		{
			FOR(k, 0, a['I' - 'A'])
				ar.push_back(9);
			a['N' - 'A'] -= tmp;	
			a['I' - 'A'] -= tmp;	
			a['N' - 'A'] -= tmp;
			a['E' - 'A'] -= tmp;
		}
		if(tmp = a['N' - 'A'])
		{
			FOR(k, 0, a['N' - 'A'])
				ar.push_back(1);
			a['O' - 'A'] -= tmp;	
			a['N' - 'A'] -= tmp;	
			a['E' - 'A'] -= tmp;
		}
		if(tmp = a['T' - 'A'])
		{
			FOR(k, 0, a['T' - 'A'])
				ar.push_back(2);
			a['T' - 'A'] -= tmp;	
			a['W' - 'A'] -= tmp;	
			a['O' - 'A'] -= tmp;
		}
		sort(ar.begin(),ar.end()); 
		cout << "Case #" << i << ": ";
		FOR(k, 0, ar.size())
			cout << ar[k];
		cout << endl;
	}
	return 0;
} 

//0 4 6 8 7 3 5 9 1 2