#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>

using namespace std;
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define foreach(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();++itr)
#define X first
#define Y second
#define PB push_back
#define MP make_pair
double doit(double c,double f,double x){
	double bst=x/2;
	double F=2,t=0;
	while(true){
		t+=c/F;
		F+=f;
		if(t+x/F<bst){
			bst=t+x/F;
		}else break;
	}
	return bst;
}
int main() {
	int Z;
	double c,f,x;
	cin>>Z;
	rep(z,Z){
		cin>>c>>f>>x;
		printf("Case #%d: %.7lf\n", z+1,doit(c,f,x));
	}
 	return 0;
}
