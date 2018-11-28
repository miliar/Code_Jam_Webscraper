#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <iterator>
#include <climits>
#include <complex>
#include <deque>
#include <iomanip>
#include <map>
#include <sstream>
using namespace std;

#define X real()
#define Y imag()

typedef complex<double> Point;
const int MaxN = 1e7 + 1;

typedef long long ll;

bool ispal(ll num)
{
	stringstream r;
	string khar ;
	r << num;
	r >> khar;
	for(int i = 0 ; i < khar.size() ; i ++)
	{
		if(khar[i] != khar[khar.size() - i - 1])
			return false;
	}
	return true;
}

unsigned long long int ans2[] ={1 , 4 , 9 , 121 , 484 , 10201 , 12321 , 14641 , 40804 , 44944 , 1002001 , 1234321 , 4008004 , 100020001 , 102030201 , 104060401 , 121242121 , 123454321 , 125686521 , 400080004 , 404090404 , 10000200001 , 10221412201 , 12102420121 , 12345654321 , 40000800004 , 1000002000001 , 1002003002001 , 1004006004001 , 1020304030201 , 1022325232201 , 1024348434201 , 1210024200121 , 1212225222121 , 1214428244121 , 1232346432321 , 1234567654321 , 4000008000004 , 4004009004004 } ;

vector<int>ans;

int main()
{
	ios_base::sync_with_stdio(false);
	for(int i = 0 ; i < 39 ; i ++)
		ans.push_back(ans2[i]);
	int n;
	cin>>n;
	for(int i = 0 ; i < n ; i ++)
	{
		ll a , b;
		cin>>a>>b;
		int a1 = lower_bound(ans.begin() , ans.end() , a) - ans.begin();
		int b1 = lower_bound(ans.begin() , ans.end() , b) - ans.begin();
		cout<<"Case #"<<i + 1<<": ";
		if(a1 == b1)
		{
			if(b == ans[b1])
				cout<<1<<endl;
			else
				cout<<0<<endl;
		}
		else 
		{
			if(b == ans[b1])
				cout<<b1 - a1 + 1<<endl;
			else
				cout<<b1 - a1<<endl;
		}
	}
}
