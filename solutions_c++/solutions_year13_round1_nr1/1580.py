#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>
using namespace std;

#define PI 3.14159265

void solve()
{
    unsigned long long r,t,c,i=0,u=0;
    cin >> r >> t;
    c = r;
    do {
        unsigned long long inner =  c * c; 
        unsigned long long outer =  (c+1) * (c+1);
        u += (outer - inner);
        c += 2;
        ++i;
    } while(u<t);
    if(u>t) --i;
    cout << i << endl;
}


int main()
{
	//srand((unsigned)time(NULL));
//	#ifdef LOCAL_TEST
		freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
//	#endif
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
//	return MAIN();
	int TestCase;
	cin >> TestCase;
	for(int CaseID = 1; CaseID <= TestCase; CaseID ++)
	{
		cout << "Case #" << CaseID << ": ";
		solve();
	}
}

