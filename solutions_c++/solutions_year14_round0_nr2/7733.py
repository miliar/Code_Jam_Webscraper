#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <sstream>
#define ll long long
using namespace std;

int gcd(int x, int y){ if(y == 0) return x; return gcd(y, x % y);}
int lcm(int x, int y){ return x * y / gcd(x, y); }

vector<int> getIntUntilEnter(){
    string line;
    getline(cin,line);
    vector<int> ins;
    int x;
    stringstream ss(line);
    while (ss >> x) ins.push_back(x);
	return ins;
}
int t;
double c,f,x;
const int INF = 1000000;
double cache[INF];
double rec(int num){
//	if(count >= INF2) return 1.0;
	double rate = 2.0 + double(num) * f;
if(rate >= 20 * x) return 1.0;
	double& ret = cache[num];
	if(ret != -1.0) return ret;
	ret = x / rate;
	for(int i = 1; c * double(i) < x; ++i){
		ret = min(ret, rec(num + i) + double(i) * c / rate);
	}
	return ret;
}

int main(){
	scanf("%d", &t);
	for(int test = 1; test <= t; ++test){
		scanf("%lf%lf%lf", &c, &f, &x);
		for(int i = 0; i < INF; ++i)
			cache[i] = -1.0;
		double ret = rec(0); 
		printf("Case #%d: %.7lf\n", test, ret);
	}
	return 0;
}
