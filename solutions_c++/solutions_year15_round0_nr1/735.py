#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <limits.h>
#include <algorithm>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <string>
#include <string.h>
#include <sstream>
#include <ctime>
 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;

int cnt,res,smax,diff,cases;
char ch;
int main()
{
	std::ios::sync_with_stdio(false);
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		res=0;
		cin>>smax;
		cin>>ch;
		cnt=ch-'0';
		for(int i=1;i<=smax;i++)
		{
			cin>>ch;
			diff=0;
			if(cnt<i)
			{
				diff=i-cnt;
			}
			res+=diff;
			cnt+=diff;
			cnt+=ch-'0';
		}
		cout<<"Case #"<<kase<<": "<<res<<"\n";
	}
	return 0;
}