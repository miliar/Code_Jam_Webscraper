/*
ID: amin_un1
PROG: ride
LANG: C++
*/

/*
my ID
uva = "sir sbu"
codforsec = "sirsbu"
topcoder = "sir_sbu"
usaco = "amin_un1"
*/
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <queue>
#include <cmath>
#include <sstream>
#include <fstream>
#include <string.h>
#include <string>
#include <map>
#include <stack>
#include <set>
#define LL long long
#define Endl endl
#define all(n) (n).begin(), (n).end()
using namespace std;
const LL mod=1000*1000*1000+7LL;
const double EXP = 1e-6;
const int MAX = 100001;
vector<LL>vec;
bool pal(LL a)
{
	LL b=0;
	LL c=a;
	while(c)
	{
		b=b*10+c%10;
		c/=10;
	}
	if(b==a)return 1;
	return 0;
}
void f()
{
	for(int i=1;i<=1000*1000*10;i++)
	{
		if(pal((long long)i*(long long)i) && pal((long long)i))
		{
			//cout<<(long long)i*(long long)i<<endl;
			vec.push_back((long long)i*(long long)i);
		}
	}
}


int main()
{
	//ofstream cout ("test.out");
    //ifstream cin ("test.in");
    //freopen("output.txt", "w", stdout);
    //freopen("input.txt", "a", stdout);
    int tc;
    cin>>tc;
    f();
    int t=0;
    //cout<<vec.size()<<endl;
    while(tc--)
    {
		t++;
		LL a,b;
		cin>>a>>b;
		int x=-1,y=-1;
		for(int i=0;i<vec.size();i++)
		{
			if(vec[i]>=a && x==-1)
			{
				//cout<<vec[i]<<" x "<<i<<endl;
				x=i;
			}
			if(vec[i]<=b)
			{
				//cout<<vec[i]<<" y "<<i<<endl;
				y=i;
			}
		}
		cout<<"Case #"<<t<<": "<<y-x+1<<endl;
	}
	return 0;
}


