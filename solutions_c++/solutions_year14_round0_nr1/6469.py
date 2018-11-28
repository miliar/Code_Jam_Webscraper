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

void scan(vector < vector <int> > & grid) {
	for (int i = 0 ; i < 4 ; i++) {
		for (int j = 0 ; j < 4 ; j++) {
			scanf("%d",&grid[i][j]) ;
		}
	}
	return ;
}

int main(int argc,char *argv[])
{
	int t;
	int l = 1;
	scanf("%d",&t) ;
	while(t--) {
		int r1,r2; 
		vector <int> a(4) ;
		vector < vector <int> > grid(4, vector <int> (4,0)) ;
		scanf("%d",&r1) ;
		scan(grid) ;
		r1-- ;
		for (int i = 0 ; i < 4 ; i++) 
			a[i] = grid[r1][i] ;
		scanf("%d",&r2) ;
		scan(grid);
		r2-- ;
		int ans = 0;
		int flag = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (flag==0 && a[i] == grid[r2][j] ) {
					ans = a[i] ;
					flag = 1;
				}
				else if (flag == 1 && a[i] == grid[r2][j]) {
					flag = 2;
					break ;
				}
			}
			if (flag == 2)
				break ;
		}
		printf("Case #%d: ",l);
		if (flag == 1)
			cout << ans << endl ;
		else if (flag == 0)
			cout << "Volunteer cheated!" << endl ;
		else if (flag == 2)
			cout << "Bad magician!" << endl ;
		
		l++ ;
	}
	return 0;
}
