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
#include <queue>
#include <assert.h>
#include <cctype>
#include <string.h>
using namespace std;

#define INF_MAX 2147483647
#define INF_MIN -2147483647

#define pi acos(-1.0)
#define INF 1e9
#define ll long long

#define For(i, a, b) for( int i = (a); i < (b); i++ )
#define Fors(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fore(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define mem(a, s) memset(a, s, sizeof (a))
#define Read() freopen("1.txt", "r", stdin)
#define Write() freopen("2.txt", "w", stdout)
#define sz(c) ((int)(c).size())
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()
#define vi vector<int>
typedef pair<int,int> PAIR;
typedef pair<PAIR ,int> PAIR2;
string tostring(long long n){ostringstream ss; ss << n; return ss.str();}
long long tonumber(string str){stringstream ss; ss << str; long long n; ss >>n; return n;}

int main()
{
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	int t;
	cin >> t;
	for (int Case = 0; Case < t; Case++)
	{
		double c,f,x;
		cin>> c >> f >> x;
		double sum=0,progress=2.0;
		double num1,num2;
		do
		{
			num1=x/progress;
			num2=c/progress +(x/(progress+f));
			if(num2 < num1)
				sum+=c/progress;
			else
				sum+=num1;
			progress+=f;
		} while (num1 > num2);
		cout << "Case #"<<Case+1<<": ";
		printf("%.7f\n",sum);
	}
	return 0;
}