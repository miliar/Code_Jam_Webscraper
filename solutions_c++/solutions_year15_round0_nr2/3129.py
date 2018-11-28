#include <iostream>
#include <fstream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#include <set>
#include <stack>
#include <queue>
#include <map>
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
#define SWAP(a,b) {int tmp=a;a=b;b=tmp;}
#define GCD(a,b)  { return (b==0)?a:GCD(b,a%b); }
#define LCM(a,b)  { return a*b/GCD(a,b);  }
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR_X(i,n,x) for(i=x;i<n;i++)
#define FORN(i,n) for(i=n;i>=0;i--)
#define FORN_X(i,n,x) for(i=n;i>=x;i--)
 
typedef long long int lld;
using namespace std;

int a[1005],mark[1005],b[1005];

int main(){

	int t,n;
	cin>>t;
	for(int k=1;k<=t;k++){
		int i,j;
		cin>>n;
		memset(mark,0,sizeof mark);
		for(i=0;i<n;i++){
			cin>>a[i];
			mark[a[i]]=mark[a[i]]+1;
		}
		
		int cost = 0, minn = INT_MAX;
		
		for(i=1;i<=1000;i++){
			
			for(j=1000;j>=1;j--)
				b[j] = mark[j];
			
			cost = 0;
			for(j=1000;j>i;j--){
				
				b[j-i] += b[j];
				cost += b[j];
					
			}
			
			if(cost + i < minn)
				minn = cost+i;
		}
		
		printf("Case #%d: %d\n",k,minn);
		
	}
	
	return 0;
	
}
	
	
