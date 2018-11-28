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
	int t,x,r,c;
	cin >> t;
	forn(j,t)
	{
		cin >> x >> r >> c;
		if (x == 1)
			cout << "Case #" << j+1 << ": GABRIEL" << endl;
		else if (x == 2)
		{
			if (r*c % 2 == 0)
				cout << "Case #" << j+1 << ": GABRIEL" << endl;
			else
				cout << "Case #" << j+1 << ": RICHARD" << endl;
		}
		else if (x == 3)
		{
			if (r > 1 and c > 1 and r*c % 3 == 0)
				cout << "Case #" << j+1 << ": GABRIEL" << endl;
			else
				cout << "Case #" << j+1 << ": RICHARD" << endl;
		}
		else if (x == 4)
		{
			if (r > 2 and c > 2 and r*c % 4 == 0)
				cout << "Case #" << j+1 << ": GABRIEL" << endl; 
			else
				cout << "Case #" << j+1 << ": RICHARD" << endl;
		}
	}
	return 0;
}
