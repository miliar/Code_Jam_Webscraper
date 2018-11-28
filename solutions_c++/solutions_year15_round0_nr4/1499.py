#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())

char res[2][30] = {"GABRIEL", "RICHARD"};

int solve(int x, int r, int c) {
  int ans=0;
  if((r*c)%x!=0) ans=1;  //X  is not a divisor
	if(x>r&&x>c) ans=1;  //Straight X doesn't fit
	int L=(x+1)/2;
	if(L>r||L>c) ans=1;	//L doesn't fit;
	if(x==4&&r*c==8) ans=1;  //T doesn't fit in 2x4
	return ans;
}

int main(){
	int run, runs;
	scanf("%d",&runs);
	for(run=1;run<=runs;run++){
		int x,r,c;
		scanf("%d %d %d",&x,&r,&c);
		int ans=solve(x,r,c);
		printf("Case #%d: %s\n",run,res[ans]);
	}
}
