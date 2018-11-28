/*
B name oooo
ID: amin_un1
PROG: ride
LANG: C++

my ID
uva = "sir sbu"
codforsec = "sir_sbu"
topcoder = "sir_sbu"
usaco = "amin_un1"
*/

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <cmath>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <bitset>
#include <complex>
#include <iomanip>
#include <time.h>
using namespace std;

#define ll long long
#define ld long double

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int MAX =100001;
const long long mod =1000*1000*1000+7;

#define mp make_pair
#define pb(a) push_back(a)
#define L(s) (int)((s).size())
#define all(c) (c).begin(), (c).end()

#define INF (1e9)
#define EPS (1e-9)
#define E (2.718281828459045)


////////////////////////////////////////////////////code///////////////////////////////////////
int main()
{
 	//ofstream cout ("test.out");
    //ifstream cin ("test.in");
    freopen("A-large.in" ,"r" , stdin);
    freopen( "output.out" , "w" , stdout );
	int tc = 0 ; 
	cin>>tc;
	int t = 0 ;
	while(tc--)
	{
		t ++;
		int n ;cin>>n;
		string s ;
		cin>>s;
		int ans = 0 , sum = 0 ;
		for(int i = 0 ; i < L(s) ; i ++)
		{
			if(sum < i  && s[i] != '0')
				ans += (i-sum) , sum = i;
			sum = sum + s[i] -(int)'0' ;
		}
		printf("Case #%d: %d\n" , t , ans);
	}
  return 0;
}
