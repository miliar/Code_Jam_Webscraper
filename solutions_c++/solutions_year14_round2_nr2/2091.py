#include <iostream>
#include <sstream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <string>
#include <map>
#include <fstream>
#include <stdlib.h>
#include <cstdio>

using namespace std;

#define ll long long
#define pb push_back
#define fl(i, n, m)		for(int i=n; i<m; i++)
#define INT_INF 2000000000
#define LL_INF 3000000000000000000

int main()
{
	int test, res;
	int a, b, k;
	cin >> test;
	for(int x=0; x<test; x++)
	{
		res = 0;
		cin >> a >> b >> k;
		for(int i=0; i<a; i++)
			for(int j=0; j<b; j++)
			{
				if((i&j) < k)
					res++;
			}
		cout << "Case #" << x+1 << ": " << res << endl;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	
}
