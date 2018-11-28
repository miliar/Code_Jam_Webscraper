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

int main()
{
	int T;
	cin>>T;

	for(int t=1;t<=T;t++){

		int k;
		string s;
		cin>>k>>s;

		long long sum=s[0]-'0';
		long long res=0;

		for(int i=1;i<s.size();i++){
			if(sum<i){res+=i-sum; sum+=i-sum;}
			sum+=s[i]-'0';
		}

		printf("Case #%d: %lld\n",t,res);
	}

	return 0;
}