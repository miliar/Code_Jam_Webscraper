#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <functional>
#include <set>
#include <sstream>
#include <map>
#include <queue>
#include <stack>

using namespace std;



long long rev(long long x)
{
	stringstream ss;
	ss<<x;
	string s=ss.str();
	

	
	reverse(s.begin(),s.end());
	
	if(s[0]=='0') return x;
	else return atol(s.c_str());
	
}

int main()
{
	int T;
	cin>>T;

	vector<long long> d(1000001LL,1000000LL);

	d[1]=1;
	for(long long i=2;i<1000000+1;i++){
		d[i]=min(d[i],d[i-1]+1);
		d[i]=min(d[i],d[rev(i)]+1);
	}

	for(int t=1;t<=T;t++){

		long long n;
		cin>>n;
		
		printf("Case #%d: %lld\n",t,d[n]);
	}

	return 0;
}