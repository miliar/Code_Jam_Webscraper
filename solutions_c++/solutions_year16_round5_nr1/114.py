#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <bitset>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
#define REP(i, a, b) for(int i = int(a); i <= int(b); i++)
#define LOOP(i, v) for(int i = 0; i < v.size(); i++)
#define EPS 1e-9
#define INF 1e12
#define debug(x) cerr << "DEBUG : " << (#x) << " => " << (x) << endl

int suiv[20005];
int prec[20005];
string s;
bool tjs[20005];
int tot;
int virer;

void parcours(int x)
{	
	if(suiv[x] < s.size() && s[x] == s[suiv[x]])
	{
		virer += 2;
		tot += 10;
		int a = prec[x];
		int b = x;
		int c = suiv[x];
		int d = suiv[suiv[x]];
		if(a != -1)
		{
			suiv[a] = d;
		}
		if(d < s.size())
		{
			prec[d] = a;
		}
		if(a != -1) parcours(a);
		else if(d < s.size()) parcours(d);
	}
	else if(suiv[x] < s.size()) parcours(suiv[x]);
}

int main()
{
	int TW;
	scanf("%d", &TW);
	
	REP(tw, 1, TW)
	{
		printf("Case #%d: ", tw);
		fprintf(stderr, "Case #%d.\n", tw);
		
		cin >> s;
		
		int t = 0;
		
		REP(i, 0, s.size()-1)
		{
			suiv[i] = i+1;
			prec[i] = i-1;
		}
		
		tot = 0;
		virer = 0;
		parcours(0);
		
		int score = tot + 5*(s.size()-virer)/2;
		
		printf("%d\n", score);
		
	}

  return 0;
}
