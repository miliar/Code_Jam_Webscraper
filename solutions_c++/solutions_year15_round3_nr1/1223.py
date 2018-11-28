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


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	std::ios::sync_with_stdio(false);
	int cases,r,c,w,res;
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>r>>c>>w;
		res=c/w;
		res*=r-1;
		res+=c/w;
		res--;
		res+=w;
		if(c%w!=0)
		{
			res++;
		}
		cout<<"Case #"<<kase<<": "<<res<<"\n";
	}
	return 0;
}