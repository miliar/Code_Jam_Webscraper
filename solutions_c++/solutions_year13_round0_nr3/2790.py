#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <iostream>

#define ln printf("\n")
typedef long long ll;

#define fr(a,b,c) for(int a = b; a < c; a++)
#define rep(a,b) fr(a,0,b)

#define dbg(x) cerr << #x << " = " << x << endl
#define db dbg
#define _  << " , " <<

using namespace std;

const double eps = 1e-6;
int n;

int cn = 1;
int r[11000000];

bool ispal(ll a){
	//if(a%100 == 0) printf("%lld\n", a);
	vector<int> d;
	
	while(a){
		d.push_back(a%10);
		a /= 10;
	}
	
	rep(i,d.size()){
		if(d[i] != d[d.size()-1-i]) return false;
	}
	
	return true;
}

void isfair(ll a){
	if(ispal(a) && ispal(a*a)){
		r[a] = 1;
		//printf("%lld\n", a);
	}
	r[a] += r[a-1];
}

ll a, b;

bool read(){
	scanf("%lld%lld", &a, &b);	
	
	return true;
}

void process(){
	printf("Case #%d: ", cn++);
	
	double st = sqrt(((double)a)) - eps + 1;
	double et = sqrt(((double)b)) + eps;
	
	int s = (int) st;
	int e = (int) et;
	
	int res = r[e] - r[s-1];
	
	//printf("%lld %lld\n", a, b);
	//printf("%d %d (%lf %lf)\n", s, e, st, et);
	
	printf("%d\n", res);
}

int main(){
	r[0] = 0;
	int hi = 11000000;
	fr(i,1,10000) isfair(i);
	
	int t = -1;
	scanf("%d", &t);
	
	while(t-- && read()){		
		process();
	}	
	
	return 0;
}
