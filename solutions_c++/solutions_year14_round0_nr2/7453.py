#include <iostream> 
#include <algorithm> 
#include <vector> 
#include <queue>
#include <stack>
#include <string> 
#include <string.h> 
#include <fstream> 
#include <map> 
#include <iomanip> 
#include <cstdio> 
#include <cstdlib>
#include <cmath>
#include <deque>
#include <set>

using namespace std; 

const int MAX = 0x7FFFFFFF; 
const int MIN = 0x80000000; 

int main()
{
	int testcase ,count = 0; 
	freopen("B-large.in", "r", stdin);
	ofstream fout("result.txt");
	cin >> testcase ; 
	while(testcase--)
	{
		count++ ; 
		double C, F, X, res = 0, t1, t2 ; 
		cin >> C >> F >> X ;  
		t1 = 2 ; 
		t2 = t1 + F ; 
		while(C/t1 + X/t2 < X/t1)
		{
			res += C/t1 ; 
			t1 = t2 ; 
			t2 += F ; 
		}
		res += X/t1 ; 
		fout << "Case #" << count << ": " << setiosflags(ios::fixed) << setprecision(7) << res << endl ;
	}
	fout.close() ; 
	return 0 ;
}