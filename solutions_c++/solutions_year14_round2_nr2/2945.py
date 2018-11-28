#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <math.h>
#include <utility>
#include <sstream>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctime>
#include <limits.h>
#include <bitset>
#include <functional>
#include <numeric>
#include <complex>
#include <fstream>
#define DELIM   '\0'
typedef long long int lld;
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		int a,b,k;
		lld count=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
			    //cout<<(i&j);
				if((i&j) < k)
					count++;
			}

		}
		cout<<"Case #"<<j<<": "<<count<<endl;

	}



	}
