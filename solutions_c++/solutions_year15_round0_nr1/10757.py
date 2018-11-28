#include<iostream>
#include<cstdlib>
#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;
int main()
{
	//freopen("sample.txt", "r", stdin);
    freopen("A-small-attempt4.in", "r", stdin);
    //freopen("B-large.in", "r", stdin);

    //freopen("output.txt", "w", stdout);
    freopen("small0.txt", "w", stdout);
    //freopen("large.txt", "w", stdout);
    
	int t,sm,sum,count;
	char s[7];
	cin>>t;
	 int n=t;
	while(t--)
	{count=0;
	sum=0;
	cin>>sm;
	for(int i=0;i<=sm;i++)
	cin>>s[i];
	s[-1]='0';
	for(int j=0;j<=sm;j++)
	{
		sum=sum+((int)s[j-1]-48);
		if(sum<j&&(int)s[j]!=48)
		{
			count=count+(j-sum);
			sum=sum+count;
		}
		
		
	}
	cout<<"Case #"<<n-t<<":"<<" "<<count<<"\n";
	
	
	}
}

