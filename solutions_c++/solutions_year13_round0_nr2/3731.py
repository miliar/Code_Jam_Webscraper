#include <iostream>
#include <cstdio>
#include <algorithm>
#include <complex>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <memory.h>
#include <iostream>
#include<list>
using namespace std;

#define pb push_back
#define sz size()

#define mset(ar,val) memset(ar,val,sizeof ar)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
int field[103][103];
int N,M;
bool check(int x,int y){
	int i;
	bool f1,f2;
	f1=f2=0;
	for(i=0;i<N;++i)
		if(field[i][y]>field[x][y])
			f1=true;
	for(i=0;i<M;++i)
		if(field[x][i]>field[x][y])
			f2=true;
	if(f1 && f2) return false;

	return true;
}
int main() {
	int T,i,j,t;
	bool isPossible;
	scanf("%d",&T);
	for(t=1;t<=T;++t){
		isPossible=true;
		cin>>N>>M;

		for(i=0;i<N;++i)
			for(j=0;j<M;++j)
				scanf("%d",&field[i][j]);

		for(i=0;i<N;++i)
			for(j=0;j<M;++j)
				if(!check(i,j)){
					isPossible=false;
					break;
				}
		if(isPossible==true)
			printf("Case #%d: YES\n",t);
		else
			printf("Case #%d: NO\n",t);

	}

	return 0;
}

