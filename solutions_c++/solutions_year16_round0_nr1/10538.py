#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

typedef vector<ld> vd;
typedef vector<vd> vvd;

typedef vector<string> vs;

const i64 d18 = 1000000000000000000LL;
const ld eps = 1e-9;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;

template <typename T>
string NumberToString ( T Number )
{
	stringstream ss;
	ss << Number;
	return ss.str();
}


void solve_case(int TN)
{
	int k;
	fin >> k;
	string s;
	fin >> s;
	int ans = 0;
	int sum = 0;
	
	
	
	FORD(i, 0, k)
	{
		if (sum < i && s[i] != '0')
		{
			ans += i-sum;
			sum = i;
		}
		sum += s[i]-'0';
	}

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

void solve_case2 (int TN) {
	
	
	//create map to store sets....
	//std::map<std::string,int> my_map;
	std::map<char,int> my_map;
	string ans = "null";
	int k;
	int N = 1;
	int temp;
	string s1;
	fin >> k;
	if (k == 0)
	{
		ans = "INSOMNIA";
	}
	else
	{
		temp = k;	
		N = 1;
		while (true)
		{
			temp = N * k;
			s1 = NumberToString (temp);
			
			FOR(jj, LEN(s1))
			{
				//cout << s1[jj] << "index " << jj  << endl;
				my_map[s1[jj]]++;
			}
			
			if (my_map.size() == 10)
			{
				
				my_map.clear();
				break;
			}
			
			/*cout << temp << endl;
			cout << s1 << endl;
			break; */
			// check if number are complete, then break;
			
			N++;
		}
		ans = NumberToString (temp);
	}
	
	fout << "Case #" << TN << ": " << ans << endl;
	//cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	
/*	
	fin.open("A.in"); 
	fout.open("A.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}
*/

	fin.open("in.txt"); 
	fout.open("out.txt");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case2(tt+1);
	}

	return 0;	
}
