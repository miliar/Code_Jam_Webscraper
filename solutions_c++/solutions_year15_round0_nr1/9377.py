#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cstring>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int tn=1;tn<=t;tn++)
	{
		int n;
		cin>>n;
		string s;
		cin>>s;
		int sum=0,ans=0;
		for(int i=0;i<n+1;i++)
		{
			if(sum<i)
				ans=ans+i-sum,sum=i;
			sum=sum+s[i]-'0';
		}
		printf("Case #%d: %d\n",tn,ans);
	}
}