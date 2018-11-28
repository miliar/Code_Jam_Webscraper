#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include<queue>
#define pii pair<int,int>
#define mk make_pair
#define pb push_back 
#define ll  long long
#define LB(v,x) lower_bound(v.begin(),v.end(),x)-v.begin()
#define UB(v,x) upper_bound(v.begin(),v.end(),x)-v.begin()
#define fi first
#define se second
#define UP 500000
using namespace std;

double acum[UP+5], R[UP+5];
int caso=1;

void doit(){
	double C,F,X;
	cin>>C>>F>>X;
	for(int i=1;i<=UP;++i){
		acum[i]=1/( 2.0+ (i-1)*F );
		acum[i]+=acum[i-1];
	}
	R[0]=0;
	for(int i=1;i<=UP;++i){
		R[i]=C*acum[i];
	}
	double best=X/2;
	if(X>C){
		for(int i=1;i<=UP;++i){
			double cur=R[i]+X/(2.0+i*F);
			if(cur>best )break;
			best=cur;
		}
	}
	printf("Case #%d: %.10lf\n",caso++,best);
}

int main(){
	int t;
	cin>>t;
	while (t--)doit();
}
