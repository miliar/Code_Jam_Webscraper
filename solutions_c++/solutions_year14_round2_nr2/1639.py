#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;


typedef long long ll;


int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin>>test;
	for(int testcase = 0; testcase<test; ++testcase)
	{

		int a,b,k;
		cin>>a>>b>>k;
		int cnt = 0;
		for(int i=0; i<a; ++i)
		{
			for(int j=0; j<b; ++j)
			{
				int tmp = i&j;
				if(tmp <k)
					cnt++;
			}
		}

		cout<<"Case #"<<(testcase+1)<<": ";
		cout<<cnt;
		cout<<"\n";
	}

	return 0;
}