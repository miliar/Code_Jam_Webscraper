#include <iostream>
#include <cstdio>
#include <set>
#include <cmath>
#include <ctime>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <cstring>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <cassert>
#include <cstdlib>


#define LL long long int
#define Li long int
#define ULL unsigned long long int
#define mp make_pair
#define pb push_back
#define forr(i,n) for(int i=0;i<int(n);i++)
#define foor(i,a,b) for(int i=int(a);i<int(b);i++)
#define infloop for(;;)
#define loop(i,s) for(auto i : s)
#define endl "\n"
#define qq_endln endl

#define gcd __gcd

#define mod 1000000007ll

using namespace std;

typedef set<int> sint;
typedef multiset<int> msint;
typedef vector<int> vint;
typedef map<int, int> mint;
typedef unordered_map<int, int> _mint;
typedef queue<int> qint;
typedef unordered_set<int> _sint;
typedef list<int> lint;
typedef pair<int, int> pint;
typedef pair<long int, long int> plint;



int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		string s;
		cin>>s;
		int gr=1;
		for(int j=0;j<s.size()-1;j++)
			if(s[j]!=s[j+1])
				gr++;
		if(s[s.size()-1]=='+')
			gr--;
		cout<<"Case #"<<i<<": "<<gr<<qq_endln;
	}
	return 0;
}


