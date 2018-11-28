//============================================================================
// Name        : Test.cpp
// Author      : Aboulkheir
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include<assert.h>
#include<string.h>
using namespace std;

int main() {
	//ios_base::sync_with_stdio(0);
	//cin.tie(0);
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin>>t;

	for(int cs=0; cs < t; cs++)
	{
		int smax;
		string ss;
		cin>>smax>>ss;

		int res=smax;
		for(int i=0; i <= smax; i++)
		{
			int cur=i+(ss[0]-'0');
			bool flag=true;
			for(int j=1; j < ss.size() && flag; j++)
			{
				if(j <= cur)
					cur+=(ss[j]-'0');
				else
					flag=false;
			}

			if(flag)
				res=min(res,i);
		}

		cout<<"Case #"<<cs+1<<": "<<res<<endl;
	}
}
