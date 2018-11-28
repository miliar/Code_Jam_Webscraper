#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <utility>
#include <string>

#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define pii pair<int, int>
#define pn(n) printf("%d\n",n)
#define sn(n) scanf("%d",&n)
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)

#define FORN(i, n) for(i = 0; i < n; i++)
#define FORAB(i,a,b) for(i = a; i <= b; i++)
	
typedef long long int li;
using namespace std;

int main(){
	int test;
	sn(test);
	int no=1;
	while(test--){

		int x;
		sn(x);
		x--;
		int a[4][4];
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				sn(a[i][j]);
			}
		}
		int y;
		sn(y);
		y--;
		int b[4][4];
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				sn(b[i][j]);
			}
		}
		int d[17];
		for (int i = 0; i < 17; ++i)
		{
			d[i]=0;
		}
		for (int i = 0; i < 4; ++i)
		{
			d[a[x][i]]++;
			d[b[y][i]]++;
		}
		int noTimesTwo=0;
		int noAns=-1;
		for (int i = 1; i < 17; ++i)
		{
			if(d[i]==2){
				noTimesTwo++;
				noAns=i;
			}
		}
		if(noTimesTwo==0){
			printf("Case #%d: Volunteer cheated!\n",no);
		}
		else if(noTimesTwo==1){
			printf("Case #%d: %d\n",no,noAns);
		}
		else if(noTimesTwo>=2){
			printf("Case #%d: Bad magician!\n",no);
		}
		no++;
	}
	return 0;
}

