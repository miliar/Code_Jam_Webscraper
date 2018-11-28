#include <string.h>
#include <queue>
#include <vector>
#include <fstream>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;
#define S(n) 		scanf("%d",&n)
#define SL(n) 		scanf("%lld",&n)
#define FORALL(i,a,b) 	for(int i=a;i<b;i++)
#define ALL(a)   	a.begin(), a.end()
#define IN(a,b) 	((b).find(a) != (b).end())
#define SZ(a) 		((int)(a.size()))
#define MP            	make_pair
#define VI 		vector<int>
#define VPI 		vector<pair<int,int> >
#define DREP(a)      	sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind) 	(lower_bound(all(arr),ind)-arr.begin())
#define LL 		long long
int findout(int a)
{
	if(a==0) return 0;
	if(a<4) return 1;
	if(a<9) return 2;
	if(a<121) return 3;
	if(a<484) return 4;
	return 5;
}
bool pal(int i)
{
	stringstream ss;
	ss<<i;
	string a=ss.str();
	string b=a;
	reverse(ALL(b));
	if(strcmp(a.c_str(),b.c_str())==0)
		return true;
	return false;
}
int pc()
{
	for(int i=1;i<=1000;i++)
	{
		if(pal(i) && pal(i*i)) cout<<i*i<<endl;
	}
}
int main()
{
	//pc();
	int t;
	ifstream fin("file.in");
	fin>>t;
	int index=0;
	while(t--)
	{
		int a,b;
		fin>>a>>b;
		cout<<"Case #"<<++index<<": "<<findout(b)-findout(a-1)<<endl;
	}
	return 0;
}
