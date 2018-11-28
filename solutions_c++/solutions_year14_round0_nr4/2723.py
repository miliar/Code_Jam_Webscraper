#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
#include "windows.h"
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "D-large";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}


int mas[4][4];

int main()
{
   init();

	int tst;
	scanf("%d",&tst);

	for (int cas = 1; cas<=tst;cas++)
	{
		vector <double> a,b;
		int n;
		cin >> n;
		for (int i=0;i<n;i++)
		{
			double t;
			cin >> t;
			a.push_back(t);		
		}
		
		for (int i=0;i<n;i++)
		{
			double t;
			cin >> t;
			b.push_back(t);		
		}

		sort(all(a));
		sort(all(b));

		int mx = 0;
		for (int i=1;i<=n;i++)
		{
			int ok = 1;
			for (int j=0;j<i;j++)
				if (a[j]>b[n-i+j]) ok = 0;
			if (ok) mx = i;		
		}

		int mx2 = 0;
		int l = 0, r = n-1;
		for (int i=0;i<n;i++)
		{
			if (b[l]>a[i])
			{
				r--;
			} else
			if (b[l]<a[i])
			{
				l++;
				mx2++;
			} else
			{
				r--;
			}
		}

		printf("Case #%d: %d %d\n",cas,mx2,n-mx);
		
	}


	
  return 0;
}

