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

ifstream fin ("A-large.in");
ofstream fout ("A-large.out");

int main()
{
	int t,smax,ans;
	char ch;
	fin>>t;
	
	rep(test,0,t)
	{
		ans = 0;
		fin>>smax;
		int count[smax];
		rep(shy,0,smax+1)
		{
			fin>>ch;
			count[shy] = getCount(ch);
			
			if((count[shy] > 0) && (count[shy-1]<shy))
			{
				ans += (shy - count[shy-1]);
				count[shy-1] +=  (shy - count[shy-1]);
			}
			
			if(shy>0)
				count[shy] += count[shy-1];
		}
		
		fout<<"Case #"<<test+1<<": "<<ans<<"\n";
	}
	
	return 0;
	
}

int getCount(char ch)
{
	switch(ch)
	{
		case '0':
		return 0;
		
		case '1':
		return 1;
		
		case '2':
		return 2;
		
		case '3':
		return 3;
		
		case '4':
		return 4;
		
		case '5':
		return 5;
		
		case '6':
		return 6;
		
		case '7':
		return 7;
		
		case '8':
		return 8;
		
		case '9':
		return 9;
	}
}


