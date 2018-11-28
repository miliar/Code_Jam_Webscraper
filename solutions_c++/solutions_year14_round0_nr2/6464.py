//Utsav Jain
//
//
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <fstream>
#include <stdlib.h>
using namespace std;

#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i) 
#define REV(i,a,b) for(int i= (int )a ; i >= (int)b ; --i)
#define REP(i,a) FOR(i,0,a)
#define INF 1000000000
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(all(container),element) != container.end())
#define tr(container,it) for(typeof(container.begin()) it=container.begin(); it!=container.end(); it++)
#define minheap(t) priority_queue< t,vector<t>,greater<t> >
#define maxheap(t) priority_queue<t>
#define pb push_back
#define ii pair<int,int>
#define ss pair<string,string>
#define F first
#define S second
#define seive(n) vector<int> prime(n+1,1);for(int i=2;i*i<n;i++) if(prime[i])  for(int j=i+i;j<n;j+=i) prime[j]=0;
#define gcd __gcd

int main(int argc,char *argv[])
{
	int t,l=1;
	scanf("%d",&t) ;
	while (t--) {
		double c,f,x ;
		scanf("%lf%lf%lf",&c,&f,&x) ;
		double time = 0;
		double rate = 2;
		while (true) {
			double t1 = 0;
			double t2 = 0; 
			t1 = x*1.0/rate ;
			t2 = c*1.0/rate + x*1.0/(rate+f) ;
		//	cout << t1 << " " << t2 << endl ;
			if ( t1 > t2) 
			{
				time += c/rate ;
				rate = rate+f ;
		//		cout << rate << " " << time << endl ;
			}
			else if ( t1 <= t2) {
				time += t1 ;
				break ;
			}
		}
		printf("Case #%d: %0.7lf\n",l,time) ;
		l++ ;
	}

	return 0;
}
