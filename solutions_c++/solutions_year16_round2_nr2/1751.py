#include <iostream>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <iomanip>
#include <sstream>

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

using namespace std;
string s1, s2;
string res1, res2;
int a=(1<<20), b=(1<<20), diff= (1<<20);
void dp(int p, int q)
{
	int status = 0;
	for(int i = p; i < s1.length(); i++)
		if(s1[i] == '?'){
			for(int j = 0; j < 10; j++)
			{
				s1[i] = j+'0';
				dp(i+1,q);
				s1[i] = '?';
			}

		}

	for(int i = q; i < s2.length(); i++)
		if(s2[i] == '?')
			for(int j = 0; j < 10; j++)
			{
				s2[i] = j+'0';
				dp(p, i+1);
				s2[i]='?';
			}


for(int i = 0; i < s1.length(); i++)
	if(s1[i] == '?' || s2[i] == '?')
		status = 1;
	
	if (status == 0)
	{
		
		int m , n;
		stringstream ss, ss2;
		ss << s1;
		ss >> m;
		ss2 << s2;
		ss2 >> n;

		if (abs(m-n) < diff)
		{
		
			diff = abs(m-n);
			a = m;
			b = n;
			res1 = s1;
			res2 = s2;
		}

		else if (abs(m-n) == diff )
		{
			if (m < a)
			{
				a = m;
				b = n;
				res1 = s1;
				res2 = s2;
			}

			 else if (m == a && n < b)
			 {
			 	a = m;
				b = n;
				res1 = s1;
				res2 = s2;
			 }
		}

	}

}


int main()
{
  int T;
 cin >> T;

 for(int t = 1; t <= T; t++ )
 {
 	cout << "Case #"<<t<<": ";
 	a=(1<<20); b=(1<<20); diff= (1<<20);
 	cin >> s1 >> s2;
 	res1.clear(); res2.clear();
 	dp(0,0);
 	cout << res1 << " " << res2 << endl;


 } 

  return 0;
}