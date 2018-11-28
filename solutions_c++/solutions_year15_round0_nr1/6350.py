#include <vector>
#include <cmath>
#include <ctype.h>
#include <cassert>
#include <ctime>
#include <climits>
#include <limits>
#include <algorithm>
#include <list>
#include <set>
#include <map>
#include <string>
#include <stdio.h>
#include <queue>
#include <stack>
#include <iomanip>
#include <bitset>
#include <utility>
#include <deque>
#include <stdlib.h>
#include <functional>
//#define C11
//#include <windows.h>

#ifdef C11
    #include <unordered_map>
    #include <unordered_set>
    #include <tuple>
#endif // C11

#define F first
#define S second
#define mp make_pair
#define pb push_back
#define fabs(x) ((x>0) ? (x) : -1*(x))
#define show(a,n) cout <<#a<<": "; for (int iii=0;iii<n;iii++) cout <<a[iii]<<" "; cout<<"\n";
#define show2(a,n,m) cout <<#a<<":\n"; for (int iii=0;iii<n;iii++) { for(int jjj=0;jjj<m;jjj++) cout <<a[iii][jjj]<<" "; cout <<"\n";}
#define name(x) cout <<#x<<" \n";
#define print(x) cout <<#x"="<<x<<"\n";
#define letters char alp[30]={qwertyuiopasdfghjklzxcvbnm},sogl[30]={qwrtpsdfghjklzxcvbnm},gl[30]={eyuioa};
#define SetBit(value,place) (value|(1<<place))
#define ClearBit(value,place) (value&(~(1<<place)))
#define InverseBit(value,place) (value^(1<<place))
#define StartClock time_t inittime=clock();
#define GetClock fprintf(stderr,"Time: %f\n",1.0*(clock()-inittime)/CLOCKS_PER_SEC);

typedef std::pair<int,int> pii;
typedef std::vector <int>::iterator iti;
typedef std::multiset <int>::iterator itm;
typedef std::set <int>::iterator itset;
typedef std::string::iterator its;
typedef std::pair<long long,long long> pll;
typedef std::vector <std::vector <int> > graph;
typedef unsigned long long ull;
typedef unsigned int ui;

using namespace std;

const int INF=INT_MAX;
const long long LINF=LLONG_MAX;
const unsigned long long ULINF=ULLONG_MAX;
const double EPS=0.000001;
const int mod=1000000007;

#define LOCAL

#ifdef LOCAL
    #include <fstream>
    ifstream cin("input.txt");
    ofstream cout("output.txt");
#else
    #include <iostream>
#endif // LOCAL

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    int t;
    cin >>t;
    int t0=t;
    while (t--)
    {
		int max_level;
		cin >>max_level;
		vector <int> levels(max_level+1,0);
		string s;
		cin >>s;
		for (int i=0;i<s.length();i++)
		{
			levels[i]=s[i]-48;
		}
		long long ans=0,curr=0;
		for (int i=0;i<=max_level;i++)
		{
			if (curr<i)
			{
				ans+=i-curr;
				curr=i;
			}
			curr+=levels[i];
		}
		cout <<"Case #"<<t0-t<<": "<<ans<<"\n";
	}
    return 0;
}
