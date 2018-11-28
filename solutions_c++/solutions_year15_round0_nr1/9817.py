#include <iostream>
#include <vector>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <unordered_set>
#include <unordered_map>


#define forn(i,n) for(int i=0;i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n); i++)
#define esta(x,v) (find((v).begin(),(v).end(),(x)) !=  (v).end())
#define index(x,v) (find((v).begin(),(v).end(),(x)) - (v).begin())
#define debug(x) cout << #x << " = "  << x << endl

typedef long long tint;
typedef unsigned long long utint;

using namespace std;

int main()
{
	int t,smax,totalUp,invite;
	string s;
	cin >> t;
	forn(j,t)
	{
		
		cin >> smax >> s;
		totalUp = 0;
		invite = 0;
		forn(i,smax+1)
		{
			if (totalUp < i)
			{
				invite += i - totalUp;
				totalUp = i;
			}
			totalUp += s[i] - '0';
		}
		cout << "Case #" << j+1 << ": " << invite << endl;
	}
	
	return 0;
}
