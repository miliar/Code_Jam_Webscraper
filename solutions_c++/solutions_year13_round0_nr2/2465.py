									/*ba yade oo */
//Mehrdad AP

#include <iostream>
#include <string>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <sstream>
#include <queue>
#include <vector>
#include <stack>
#include <set>
#include <map>



using namespace std;

#define PI 3.14159265358997
#define absol(x) ((x)>(0) ? (x):(-1)*(x))
#define pow2(x) ((x)*(x))
#define EPS 1e-7
#define INF 100000000
#define MAX 10000
#define MODE 1000000007
#define Left(x) (2*x)
#define Right(x) ((2*(x)+1)
//#define inRange(x,y) (x>=0 && x<N && y>=0 && y<M)

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;
typedef long long int lli;

int N,M;
int A[MAX][MAX];

bool allColLess(int x,int num){

	for (int i=0;i<N;i++){
		if (A[i][x]>num) return false;
	}
	return true;
}

bool allRowLess(int x,int num){

	for (int i=0;i<M;i++){
		if (A[x][i]>num) return false;
	}
	return true;
}

int main ()
{
	
	int  tc,TC=0;
	cin>>tc;
	while (tc--){

		cin>>N>>M;

		for (int i=0;i<N;i++)
			for (int j=0;j<M;j++) 
				scanf("%d",&A[i][j]);

		bool can=true;
		for (int x=100;x>=1 && can;x--){

			for (int i=0;i<N && can;i++)
				for (int j=0;j<M && can;j++){
					if (A[i][j]==x){
						if (!( allRowLess(i,x) || allColLess(j,x)))
							can=false;
					}
				}
		}
		
		printf("Case #%d: %s\n",++TC,(can ? "YES":"NO"));
	}
	return 0;
}
