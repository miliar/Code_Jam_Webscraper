


#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <iostream>

#include <algorithm>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define EPS 0.000000001
#define INF 1000000000

int n;
string richard = "RICHARD";
string gabriel = "GABRIEL";

string getAnswer(int x, int r, int c)
{
	if (x==1) return gabriel;
	
	int m = r*c;
	
	if (m%x!=0) return richard;
	
	if (m==1) return richard;
	
	if (m==2) {
		if (x==2) return gabriel;
		return richard;
	}
	
	if (m==3) {
		return richard;
	}
	
	if (m==4) {
		if (x>2) return richard;
		return gabriel;
	}
	
	if (m==6) {
		if (x==4) return richard;
		return gabriel;
	}
	
	if (m==8) {
		if (x>2) return richard;
		return gabriel;
	}
	
	if (m==9) {
		if (x==2||x==4) return richard;
		return gabriel;
	}
	
	if (m==12) {
		return gabriel;
	}
	
	if (x==3) return richard;
	return gabriel;
}

int main() {
	
	int T;
	cin>>T;
	int caseNum=0;
	
	int X, R, C;
	
	while (T-->0)
	{
		cin>>X>>R>>C;
//		printf("X %d R %d C %d\n", X, R, C);
		cout<<"Case #"<<++caseNum<<": "<<getAnswer(X, R, C)<<endl;
	}
	
	return 0;
}

