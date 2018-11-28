/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
   * File Name : ARRANGE.cpp
   * Creation Date : 19-12-2013
   * Last Modified : Saturday 12 April 2014 06:57:12 PM IST

   _._._._._._._._._._._._._._._._._._._._._.*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>

#define FREE(p) \
	    free(p);    \
    p = NULL;
#define sz(a) int((a).size())
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define FILL(x,y) memset(&x,y,sizeof(x)) //example( FILL(buffer,-1) )
#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; i++)
#define rep(i,n) 	FOR(i,0,n)
#define si(n) scanf("%d",&n)
#define pil(n) printf("%d\n",n)//print integer
#define sl(n) scanf("%lld",&n)//long long int
#define sd(n) scanf("%lf",&n)//double
#define ss(n) scanf("%s",n)
#define sc(ch) scanf("%c",&ch)
#define ps(s) printf("%s\n",s)//print string
#define pc(s) printf("%c",s)//print character
#define sln printf("\n"); 
#define PB push_back
#define MP make_pair
#define scan(v,n)	vector<int> v;rep(i,n){ int j;si(j);v.PB(j);}
typedef long long int LL;
using namespace std;
typedef vector <int> VI;
typedef pair < int ,int > PII;
typedef vector < PII > VPII;

int main()
{
	int i,j,z,test;
	si(test);
	double C,F,X,sum,temp;
	rep(z,test)
	{
		sum=0.0;
		sd(C);sd(F);sd(X);
		i=1;

		temp = C/2.0;
		sum =  X/2.0;
		while(temp +X/(2+i*F) < sum)
		{
			sum=temp + X/(2+i*F);
			temp+= C/(2+i*F);
			i++;
		}
		printf("Case #%d: %0.7lf\n",z+1,sum);

	}
		return 0;
}
