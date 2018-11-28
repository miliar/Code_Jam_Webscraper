
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
#include <list>
#include <cassert>



using namespace std;
#pragma comment(linker, "/STACK:50000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-large(3)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}



int main()
{
	init();

	int tst;
	scanf("%d\n",&tst);

	for (int cas = 1; cas<=tst;cas++)
	{

		char st[111];
		gets(st);
		string s = st;

		int res = 0;
		for (int i=0;i<sz(s)-1;i++)
			if (s[i]=='+' && s[i+1]=='-') res+=2;
		if (s[0]=='-') res++;
		
		printf("Case #%d: %d\n",cas,res);
		
	
	}


	return 0;
}
