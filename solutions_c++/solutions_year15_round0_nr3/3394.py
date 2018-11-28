#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <cstring>
#include <memory.h>
#include <bitset>
#include <time.h>
#define sf(x) scanf("%d", &x)
#define sff(x) scanf("%lf", &x)
#define sfc(x) scanf(" %c", &x)
#define pf(x) printf("%d ", x)
#define pff(x) printf("%lf", x)
#define pfc(x) printf("%c", x)
#define pfs(x) printf("%s", x)
#define sfl(x) scanf("%I64d", &x)
#define sfl2(x,y) scanf("%I64d %I64d", &x,&y)
#define ENDL printf("\n")
#define INF 2147483647
#define pf2(x,y) printf("%d %d", x,y)
#define sf2(x,y) scanf("%d %d", &x,&y)
#define pb(x) push_back(x)
#define ppb() pop_back()
#define mp(x,y) make_pair(x,y)
#define sf3(x,y,z) scanf("%d %d %d", &x,&y,&z)
#define print(x) puts(#x)
#define error(x) cerr<<#x<<' '<<x<<'\n'


using namespace std;

typedef long long ll; 
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef vector<int> vec;


char mul(char a, char b)
{
	if(a=='1') return b;
	if(a==-'1') return -b;
	if(b=='1') return a;
	if(b==-'1') return -a;
	if(a=='i'&&b=='j')
	return 'k';
	if(a=='i'&&b=='k')
	return -'j';
	if(a=='j'&&b=='i')
	return -'k';
	if(a=='j'&&b=='k')
	return 'i';
	if(a=='k'&&b=='i')
	return 'j';
	if(a=='k'&&b=='j')
	return -'i';
}


int main()
{
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	/**/
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
    	int l,x;
    	sf2(l,x);
    	string s;
    	string qwe;
    	cin>>qwe;
    	for(int i=0; i<x; i++)
    	{
    		s+=qwe;
    	}
    	printf("Case #%d: ",t);
    	char res='1';
		for(int i=0; i<s.size(); i++)
		{
			if(res==s[i]) res=-'1';
			else if(res==-s[i]) res='1';
			else if(res<0) res=-mul(-res, s[i]);
			else res=mul(res,s[i]);
		}
		if(res!=-'1')
		{
			print(NO);
			continue;
		}
		res='1';
		int pos1=0;
		for(int i=0; i<s.size(); i++)
		{
			if(res==s[i]) res=-'1';
			else if(res==-s[i]) res='1';
			else if(res<0) res=-mul(-res, s[i]);
			else res=mul(res,s[i]);
			pos1=i;
			if(res=='i')
			{
				break;
			}
		}
		res='1';
		int pos2=s.size()-1;
		for(int i=s.size()-1; i>=0; i--)
		{
			if(res==s[i]) res=-'1';
			else if(res==-s[i]) res='1';
			else if(res<0) res=-mul(s[i],-res);
			else res=mul(s[i],res);
			pos2=i;
			if(res=='k')
			{
				break;
			}
		}
		if(pos2<=pos1+1)
		print(NO);
		else
		print(YES);
    }
    return 0;
}












