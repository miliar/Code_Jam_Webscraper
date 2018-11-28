#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <limits.h>

using namespace std;

#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define vi vector<int>
#define pb push_back
#define ll long long int
#define gi(x) scanf("%d",&x)
#define ii pair<int,int>
#define CLEAR(x,val) memset(x,val,sizeof(x))
#define SZ(v) (v).size()
#define MOD 1000000000
#define MAXN 66000

int getCount(char);

//ifstream fin ("input.txt");
//ofstream fout("output.txt");
ifstream fin ("B-large.in");
ofstream fout ("B-large.out");

int main()
{
	int t,d,p,total,ans;
	char ch;
	fin>>t;
	
	rep(test,0,t)
	{
		ans = MOD;
		fin>>d;
		int arr[d];
		rep(i,0,d)
		{
			fin>>arr[i];
		}
		
		rep(m,1,1007)
		{
			int time =0;
			rep(i,0,d)
			{
				time += (arr[i]/m)-1 + ((arr[i]%m) ? 1 : 0);
			}
			
			//cout<<m+time<<"\n";
			ans = min(ans , m+time);
			
		}
		
		fout<<"Case #"<<test+1<<": "<<ans<<"\n";
	}
	
	return 0;
	
}


