
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

string problem_name = "D-small-attempt0(1)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}


long long calc(string s, int p)
{
	long long res = 0;
	for (int i=0;i<sz(s);i++)
	{
		if (s[i]=='1') res++;
		res*=p;
	}
	return 0;
}

int main()
{
	init();

	int tst;
	scanf("%d\n",&tst);

	for (int cas = 1; cas<=tst;cas++)
	{

		int k,c,s;
		scanf("%d%d%d",&k,&c,&s);
		
		printf("Case #%d:",cas);
		for (int i=1;i<=s;i++)
			printf(" %d",i);
		printf("%\n");
		
	
	}


	return 0;
}
