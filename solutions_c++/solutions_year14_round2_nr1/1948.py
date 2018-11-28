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
	int t;
	scanf("%d",&t) ;
	int r =0 ;
	while(t--) {
		r++ ;
		int n;
		scanf("%d",&n) ;
		string a,b ;
		cin >> a >> b ;
		int cnt = 0 ;
		int l = a.size() ; 
		int m = b.size() ;
		int i = 0 ;
		int k = 0 ;
		int flag = 0 ;
		while ( i < l && k < m ) {
			while (i < l && k < m &&  a[i] == b[k]) {
				i++ ;
				k++ ;
			}
			//cout << "Equal :" << i << " " << k << endl ;
			while (i < l && i > 0 && a[i] == a[i-1] ) {
				cnt++ ;
				i++ ;
			}
			//cout << "First String:" << i << " " << k << endl ;
			while (k < m && k > 0 && b[k] == b[k-1] ) {
				cnt++ ;
				k++ ;
			}
			//cout << "Second String:" << i << " " << k << endl ;
			if ( a[i] != b[k] ) {
				flag = 1 ;
				break ;
			}
		}
		if (flag == 0) 
			printf("Case #%d: %d\n",r,cnt) ;
		else 
			printf("Case #%d: Fegla Won\n",r) ;
	}

	return 0;
}
