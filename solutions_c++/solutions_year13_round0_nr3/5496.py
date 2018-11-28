/*
	Name: ONUR YILDIZ
 	School: Fatih Koleji
	Country: Turkiye
*/

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <cstring>

#define p_q priority_queue
#define SFOR(i,a) for(i=a.begin();i!=a.end();++i)
#define VFOR(i,a) for(i=0;i<a.size();i++)
#define FOR(a,b,c) for(a=b;a<=(int)c;a++)
#define ROF(a,b,c) for(a=b;a>=(int)c;a--)
#define FILL(a,b) memset(a,b,sizeof(a))
#define Vall(v) v.begin(),v.end()
#define Aall(A,N) A+1,A+N+1
#define pii pair < int , int > 
#define pll pair <  ll ,  ll >
#define pdd pair < dbl , dbl >
#define vii vector < pii >
#define si set < int >
#define vi vector< int >
#define dbl double
#define ll long long
#define INF (int)1e9
#define LINF (ll)1e16
#define sqr(a) ((a)*(a))
#define mkp make_pair
#define pb push_back
#define f first
#define s second
#define eps 1e-6
#define b(a,b) ( (a)-(b) > +eps)
#define k(a,b) ( (a)-(b) < -eps)
#define e(a,b) ( k(a,b) && k(b,a) )

using namespace std;

int N,__T;

bool pal(int k)
{
	int a=k,b=0;
	while(k)
	{
		b=b*10+k%10;
		k/=10;
	}
	return a==b;
}

int main()
{
	int i,j,q,s,A,B;
	scanf(" %d",&__T);
	FOR(q,1,__T)
	{
		//CLEAR
		scanf(" %d %d",&A,&B);
		s=0;
		FOR(i,1,B)
		{
			if(i*i < A) continue;
			if(i*i > B) break;
			if(pal(i) && pal(i*i)) s++;
		}
		printf("Case #%d: %d\n",q,s);
	}

	return 0;
}
