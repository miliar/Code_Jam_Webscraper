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
using namespace std;
#pragma comment(linker, "/STACK:50000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "A-large";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}



int main() {

	init();


	
	int tst;
	scanf("%d\n",&tst);

	for (int cas = 1; cas<=tst;cas++)
	{
		char st[10000];
		string s;

		int mx;
		scanf("%d ",&mx);
		gets(st);
		//puts(st);
		s = st;
		int res = 0;
		int cur = 0;
		for (int i=0;i<=mx;i++)
		{
			if (s[i]!='0')
			{
				if (cur>=i)
				{
					cur+=s[i]-'0';
				} else
				{
					res+=i-cur;
					cur=cur + (i-cur) + s[i]-'0';
				}
			}
		}	

		printf("Case #%d: %d\n",cas,res);
	}
	
	
	
	

	return 0;
}

