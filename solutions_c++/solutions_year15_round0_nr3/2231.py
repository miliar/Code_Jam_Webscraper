#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
#include <cstring>

using namespace std;

#define DECL(v, c)					decltype(c) v = c

// Util Constants
#define INF							(int)1e9
#define EPS							1e-9
#define PI 							3.1415926535897932384626

// Math Shortcuts
#define MAX(a,b)					((a) > (b) ? (a) : (b))
#define MIN(a,b)					((a) < (b) ? (a) : (b))
#define ABS(v)						((v) < 0 ? (-v) : (v))

// Bit Operations
#define BIT(v,b)					((v) & (1 << b)) //select the bit of position i of x
#define LOWBIT(v) 					((v) & ((v) ^ ((v) - 1))) //get the lowest bit of x

// Bound Checking
#define IN(i,l,r) 					(l < i && i < r) 
#define LINR(i,l,r) 				(l <= i && i <= r)
#define LIN(i,l,r) 					(l <= i && i < r)
#define INR(i,l,r) 					(l < i && i <= r)

// Loops
#define FOR(i,s,n)					for(int (i) = ((int)(s)); (i) < ((int)n); (i)++)
#define DFOR(i,s,n)					for(int (i) = ((int)(n)) - 1; i >= ((int)s); (i)--)

// Iterations
#define FOREACH(v, c)				for(DECL(v, (c).begin()); v != (c).end(); ++v)
#define DFOREACH(v, c)				for(DECL(v, (c).rbegin()); v != (c).rend(); ++v)

// Container Operations
#define SZ(c)						((int)(c.size()))
#define ALL(c)						(c).begin(), (c).end()
#define RALL(c)						(c).rbegin(), (c).rend()
#define ISIN(v,c)					((c).find(v) != (c).end())
#define ISIN2(v,c)					(find(ALL(c),v) != (c).end())

// Vector Operations
#define PB							push_back
#define LAST(c)						c[SZ(c) - 1]

// Pair Operations
#define MP							make_pair
#define FI							first
#define SE							second

// Debug
#define D(a)						cerr << #a << " = " << a << endl;
template<typename T1, typename T2> inline ostream& operator << (ostream& os, const pair<T1, T2>& p) {return os << "(" << p.FI << ", " << p.SE << ")";}
template<typename T> inline ostream &operator << (ostream & os,const vector<T>& v) {bool first = true; os << "[";FOR(i,0,SZ(v)){if(!first)os << ", ";os << v[i];first = false;}return os << "]";}
template<typename T> inline ostream &operator << (ostream & os,const set<T>& v) {bool first = true;os << "[";FOREACH(ii,v){if(!first)os << ", ";os << *ii;first = false;} return os << "]";}
template<typename T1, typename T2> inline ostream &operator << (ostream & os,const map<T1, T2>& v) {bool first = true;os << "[";FOREACH(ii,v){if(!first)os << ", ";os << *ii ;first = false;}return os << "]";}

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef pair<string,string> pss;

inline string mult(string a, string b)
{
	if (a == "1")
	{
		if (b == "1")
		{
			return "1";
		}
		
		if (b == "i")
		{
			return "i";
		}
		
		if (b == "j")
		{
			return "j";
		}
		
		if (b == "k")
		{
			return "k";
		}
		
		if (b == "-1")
		{
			return "-1";
		}
		
		if (b == "-i")
		{
			return "-i";
		}
		
		if (b == "-j")
		{
			return "-j";
		}
		
		if (b == "-k")
		{
			return "-k";
		}
	}

	if (a == "i")
	{
		if (b == "1")
		{
			return "i";
		}
		
		if (b == "i")
		{
			return "-1";
		}
		
		if (b == "j")
		{
			return "k";
		}
		
		if (b == "k")
		{
			return "-j";
		}
		
		if (b == "-1")
		{
			return "-i";
		}
		
		if (b == "-i")
		{
			return "1";
		}
		
		if (b == "-j")
		{
			return "-k";
		}
		
		if (b == "-k")
		{
			return "j";
		}
	}

	if (a == "j")
	{
		if (b == "1")
		{
			return "j";
		}
		
		if (b == "i")
		{
			return "-k";
		}
		
		if (b == "j")
		{
			return "-1";
		}
		
		if (b == "k")
		{
			return "i";
		}
		
		if (b == "-1")
		{
			return "-j";
		}
		
		if (b == "-i")
		{
			return "k";
		}
		
		if (b == "-j")
		{
			return "1";
		}
		
		if (b == "-k")
		{
			return "-i";
		}
	}

	if (a == "k")
	{
		if (b == "1")
		{
			return "k";
		}
		
		if (b == "i")
		{
			return "j";
		}
		
		if (b == "j")
		{
			return "-i";
		}
		
		if (b == "k")
		{
			return "-1";
		}
		
		if (b == "-1")
		{
			return "-k";
		}
		
		if (b == "-i")
		{
			return "-j";
		}
		
		if (b == "-j")
		{
			return "i";
		}
		
		if (b == "-k")
		{
			return "1";
		}
	}

	if (a == "-1")
	{
		if (b == "1")
		{
			return "-1";
		}
		
		if (b == "i")
		{
			return "-i";
		}
		
		if (b == "j")
		{
			return "-j";
		}
		
		if (b == "k")
		{
			return "-k";
		}
		
		if (b == "-1")
		{
			return "1";
		}
		
		if (b == "-i")
		{
			return "i";
		}
		
		if (b == "-j")
		{
			return "j";
		}
		
		if (b == "-k")
		{
			return "k";
		}
	}

	if (a == "-i")
	{
		if (b == "1")
		{
			return "-i";
		}
		
		if (b == "i")
		{
			return "1";
		}
		
		if (b == "j")
		{
			return "-k";
		}
		
		if (b == "k")
		{
			return "j";
		}
		
		if (b == "-1")
		{
			return "i";
		}
		
		if (b == "-i")
		{
			return "-1";
		}
		
		if (b == "-j")
		{
			return "k";
		}
		
		if (b == "-k")
		{
			return "-j";
		}
	}

	if (a == "-j")
	{
		if (b == "1")
		{
			return "-j";
		}
		
		if (b == "i")
		{
			return "k";
		}
		
		if (b == "j")
		{
			return "1";
		}
		
		if (b == "k")
		{
			return "-i";
		}
		
		if (b == "-1")
		{
			return "j";
		}
		
		if (b == "-i")
		{
			return "-k";
		}
		
		if (b == "-j")
		{
			return "-1";
		}
		
		if (b == "-k")
		{
			return "i";
		}
	}
	
	if (a == "-k")
	{
		if (b == "1")
		{
			return "-k";
		}
		
		if (b == "i")
		{
			return "-j";
		}
		
		if (b == "j")
		{
			return "i";
		}
		
		if (b == "k")
		{
			return "1";
		}
		
		if (b == "-1")
		{
			return "k";
		}
		
		if (b == "-i")
		{
			return "j";
		}
		
		if (b == "-j")
		{
			return "-i";
		}
		
		if (b == "-k")
		{
			return "-1";
		}
	}
	
	return "LA MANQUEASTE";
}

bool solve()
{
	tint  l, x;
	string input;
	
	cin >> l >> x;	
	cin >> input;		
		
	if (x > 50)
	{
		x = (x % 4) + 40;
	}
	
	string input_ext = input;
	
	FOR(i,0,x - 1)
	{
		input_ext += input;
	}
	
	int total_l = l * x;
	
	if (total_l < 3)
	{
		return false;
	}
	
	vs va(total_l);
	vs vb(total_l);
		
	int curr_a = 0;
	int curr_b = total_l - 1;
	
	va[curr_a] = input_ext[curr_a];
	vb[curr_b] = input_ext[curr_b];
	
	curr_a++;
	curr_b--;
	
	FOR(i,1,total_l)
	{		
		va[curr_a] = mult(va[curr_a - 1], string(1, input_ext[i]));		
		vb[curr_b] = mult(string(1, input_ext[total_l - i - 1]), vb[curr_b + 1]);
		
		curr_a++;
		curr_b--;
	}
				
	FOR(i,0,total_l-2)
	{
		if (va[i] == "i" && vb[i + 1] == "i")
		{			
			vs vc(total_l - i - 1);
			vc[0] = input_ext[i + 1];
			
			FOR(j,1,total_l - i - 1)
			{
				vc[j] = mult(vc[j - 1], string(1, input_ext[j + i + 1]));
			}
			
			FOR(j,0,total_l - i - 2)
			{
				
				if (vc[j] == "j" && vb[i + 1 + j + 1] == "k")
				{
					return true;
				}
			}
			
		}
	}
	
	return false;
}

int main()
{
	DECL(ncas,0);
	cin >> ncas;
	
	string line;
	getline(cin, line);
	
	FOR(cas,1,ncas + 1)
	{
		cout << "Case #" << cas << ": ";		
		
		// Code here
		
		cout << (solve() ? "YES" : "NO");
		
		// End Code
		
		cout << endl;
	}

	return 0;
}