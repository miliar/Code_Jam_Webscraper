/*
ID: behdad.1
LANG: C++11
PROB: 
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <queue>
#include <deque>
#include <math.h>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <string>
#include <string.h>
#include <limits.h>
#include <time.h>
#include <complex>

#define For(i,a,b) for(int i = a; i < b; i++)
#define Fori(i,s) for(auto i = s.begin(); i != s.end(); i++)
#define roF(i,b,a) for(int i = b; i >= a; i--)
#define roFi(i,s) for(auto i = s.rbegin(); i != s.rend(); i++)
#define trace(x) cout<<#x<<": "<<x<<endl;
#define _ <<" :: "<<
#define allof(x) x.begin(),x.end()
#define X real()
#define Y imag()

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

ifstream fin("file.in");
ofstream fout("file.out");

int main()
{
	int t;
	cin >> t;
	For(tt,1,t+1)
	{
		vi nums;
		nums.assign(26,0);
		string s;
		cin >> s;
		For(i,0,s.size())
			nums[s[i]-'A']++;
		vi res;
		For(i,0,nums['Z'-'A'])
			res.push_back(0);
		int k = nums['Z' - 'A'];
		nums['O' - 'A'] -= k;

		For(i,0,nums['W'-'A'])
			res.push_back(2);
		k = nums['W' - 'A'];
		nums['T' - 'A'] -= k;
		nums['O' - 'A'] -= k;

		For(i,0,nums['G'-'A'])
			res.push_back(8);
		k = nums['G' - 'A'];
		nums['T' - 'A'] -= k;
		
		For(i,0,nums['U'-'A'])
			res.push_back(4);
		k = nums['U' - 'A'];
		nums['F' - 'A'] -= k;
		nums['O' - 'A'] -= k;

		For(i,0,nums['F'-'A'])
			res.push_back(5);
		k = nums['F' - 'A'];
		nums['V' - 'A'] -= k;

		For(i,0,nums['V'-'A'])
			res.push_back(7);
		k = nums['V' - 'A'];
		nums['S' - 'A'] -= k;
		nums['N' - 'A'] -= k;

		For(i,0,nums['S'-'A'])
			res.push_back(6);
		
		For(i,0,nums['O'-'A'])
			res.push_back(1);
		k = nums['O' - 'A'];
		nums['N' - 'A'] -= k;

		For(i,0,(nums['N'-'A']/2))
			res.push_back(9);
		
		For(i,0,(nums['T'-'A']))
			res.push_back(3);
		
		sort(allof(res));

		fout << "Case #" << tt << ": "; 
		For(i,0,res.size())
			fout << res[i];
		fout << endl;
	}
	
}
