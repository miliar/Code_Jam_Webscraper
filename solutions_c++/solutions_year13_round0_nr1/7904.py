#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include<sstream>
#include <string>
#include<numeric>
#include<stack>
#include<iomanip>
#define FOR(i,x,y) for (int i = x; i < y; i++)
#define all(v) (v).begin(), (v).end()
#define oo (1<<30)
#define eps (1e-9)
 
using namespace std;

char A[4][4];

bool check(char x){
	FOR(i,0,4){
		int c1=0,c2=0;
		FOR(j,0,4){
			//cout<<A[i][j];
			if(A[i][j]==x||A[i][j]=='T')c1++;
			if(A[j][i]==x||A[j][i]=='T')c2++;
		}
		
		if(c1==4||c2==4)return 1;
	}
	int c1=0,c2=0;
	FOR(i,0,4){
		if(A[i][i]==x||A[i][i]=='T')c1++;
		if(A[i][4-i-1]==x||A[i][4-i-1]=='T')c2++;
	}
	if(c1==4||c2==4)return 1;
	return 0;
}

int main ()
{
	int T;
	scanf("%d",&T);
	FOR(i,0,T){
		bool x=0,o=0;	
		bool comp=1;
		FOR(j,0,4)FOR(r,0,4){cin>>A[j][r];if(A[j][r]=='.')comp=0;}
		if(check('X'))printf("Case #%d: X won\n",i+1);
		else{
			if(check('O'))printf("Case #%d: O won\n",i+1);
			else{
				if(comp)printf("Case #%d: Draw\n",i+1);
				else printf("Case #%d: Game has not completed\n",i+1);
			}
		}
	}
	return 0;
}
