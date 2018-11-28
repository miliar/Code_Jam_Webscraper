#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <complex>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <climits>
#include <ctime>
using namespace std;

#define IN_THE_SET(_set,_val) (_set.find(_val) != _set.end())

int cases , Case = 1;
////////////

char check(long long a)
{
	stringstream ss;
	ss << a;
	string as = ss.str();
	int n = as.size();
	for(int i = 0 ; i < n/2; ++i)
	{
		if( as[i] != as[n-i-1])
			return 0;
	}
	return 1;
}

void aaa()
{
	int cnt = 0;
	for(long long i = 1 ; i <= 10000000; ++i)
	{
		if( check(i) && check(i*i) )
		{
			//cout << i << " " << i*i << endl;
			printf("%lld," , i*i);
			++cnt;
		}
	}
	cout << cnt;
}

const int n = 39; //miku
long long all[]={
1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,
10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,
1214428244121,1232346432321,1234567654321,4000008000004,4004009004004
};

int main()
{	
	//aaa(); return 0;
	scanf("%d" , &cases);	
	while( cases-- )
	{
		printf("Case #%d: " , Case++);   
		long long a , b;
		cin >> a >> b;
		int ans=0;
		for(int i = 0 ; i < n; ++i)
		{
			if( all[i] <= b && all[i] >= a )
				++ans;
		}
		
		cout << ans << endl;
	}


	return 0;
}
