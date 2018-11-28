/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
   * File Name : ARRANGE.cpp
   * Creation Date : 19-12-2013
   * Last Modified : Saturday 12 April 2014 05:50:50 PM IST

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
	int i,j,z,test,num,pos;
	si(test);
	map<int,int> a;
	VI v;
	rep(z,test)
	{
		a.clear();
		v.clear();
		si(pos);
		rep(i,4)
		{
			rep(j,4)
			{
				si(num);
				if(i==pos-1)
					a[num]++;
			}
		}
		si(pos);
		rep(i,4)
		{
			rep(j,4)
			{
				si(num);
				if(i==pos-1)
				{
				if(a.find(num)!=a.end())
					v.PB(num);
				}
			}
		}
		if(v.size()==0)
			printf("Case #%d: Volunteer cheated!\n",z+1);
		else if(v.size()==1)
			printf("Case #%d: %d\n",z+1,v[0]);
		else
			printf("Case #%d: Bad magician!\n",z+1);
	}


		return 0;
}
