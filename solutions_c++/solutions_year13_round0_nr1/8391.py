

/* Author:
       * Rohit Laddha */
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <limits.h>
#include <math.h>
#include <cassert>
#include <ctime>
#include <queue>
#include <tr1/random>
#include <tr1/unordered_map>
using namespace std;
using namespace std::tr1;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << x << endl;
#define PI 3.14159265

int main(){
	int t;
	scanf("%d",&t);
	for(int z=1;z<=t;z++){
		char a[4][4];
		for(int i=0;i<4;i++)
			scanf("%s",a[i]);
		int x=0,o=0,dot=0;
		bool flag=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(a[i][j]=='X')
					x++;
				else if(a[i][j]=='O')
					o++;
				else if(a[i][j]=='.')
					dot++;
			}
			if(x>=3 && o==0){
				printf("Case #%d: X won\n",z);
				flag=1;
				break;
			}
			else if(o>=3 && x==0){
				printf("Case #%d: O won\n",z);
				flag=1;
				break;
			}
		}
		if(flag==1)
			continue;
		for(int j=0;j<4;j++){
			x=0,o=0;
			for(int i=0;i<4;i++){
				if(a[i][j]=='X')
					x++;
				else if(a[i][j]=='O')
					o++;
			}
			if(x>=3 && o==0){
				printf("Case #%d: X won\n",z);
				flag=1;
				break;
			}
			else if(o>=3 && x==0){
				printf("Case #%d: O won\n",z);
				flag=1;
				break;
			}
		}
		if(flag==1)
			continue;
		x=0,o=0;
		for(int i=0;i<4;i++){
			if(a[i][i]=='X')
				x++;
			else if(a[i][i]=='O')
				o++;
			if(x>=3 && o==0){
				printf("Case #%d: X won\n",z);
				flag=1;
			}
			else if(o>=3 && x==0){
				printf("Case #%d: O won\n",z);
				flag=1;
				break;
			}
		}
		if(flag==1)
			continue;
		x=0,o=0;
		for(int i=0;i<4;i++){
			if(a[i][3-i]=='X')
				x++;
			else if(a[i][3-i]=='O')
				o++;
			if(x>=3 && o==0){
				printf("Case #%d: X won\n",z);
				flag=1;
			}
			else if(o>=3 && x==0){
				printf("Case #%d: O won\n",z);
				flag=1;
				break;
			}
		}
		if(flag==1)
			continue;
		if(dot>0)
			printf("Case #%d: Game has not completed\n",z);
		else
			printf("Case #%d: Draw\n",z);
	}
	return 0;
}
