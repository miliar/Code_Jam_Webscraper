#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0; i<n; i++)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORR(i,a,b) for (int i=a; i>=b; i--)
#define pi M_PI

typedef long long ll;
typedef vector<int> VI;
typedef vector<ll> VL;
typedef vector<VI> VVI;
typedef pair<int,int> PII;

int main(void) {
	FILE *fp;
	fp = fopen("out.txt","w");
	fprintf(fp,"Case #1:\n");
	int j=0, n=16;
	int x1=0, x2=0, y1=0, y2=1;
	while(j<500){
		if(x1==n-3 && x2==n-2){
			y2++;
			x1=0;
			x2=1;
		}else if(x2<n-2){
			x2++;
		}else{
			x1++;
			x2=x1+1;
		}
		int a[32]={};
		a[0] = a[2*n-1] = 1;
		a[2*(x1+1)] = a[2*(x2+1)] = 1;
		a[2*y1+1] = a[2*y2+1] = 1;
		REP(i,2*n){
			fprintf(fp,"%d",a[i]);
			cout << a[i];
		}
		cout << endl;
		fprintf(fp," 3 2 3 2 7 2 3 2 3\n");
		j++;
	}

	return 0;
}