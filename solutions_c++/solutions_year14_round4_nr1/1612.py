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

string problem_name = "A-large(1)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

multiset <int> m;

int main()
{
	init();


	int tst;
	scanf("%d",&tst);
	
	for (int cas = 1; cas<=tst;cas++)
	{
		int res = 0;

		m.clear();
		int n,x;
		scanf("%d%d",&n,&x);
		vi mas;
		for (int i=0;i<n;i++)
		{
			int t;
			scanf("%d",&t);
			m.insert(t);
		}

		res =n;
		while (sz(m)>=2)
		{
			multiset <int> :: iterator it = m.end();
			it--;
			int val = *it;
			m.erase(it);
			

			multiset <int> :: iterator it2 = m.lower_bound(x-val);
			if (it2!=m.begin()) it2--;
			{
				if (val + *it2 <=x) {
					res--;
					m.erase(it2);
				}
			}	
		}

		printf("Case #%d: %d\n",cas, res);	
	}

	


	
  return 0;
}

