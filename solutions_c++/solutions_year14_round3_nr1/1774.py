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

int main(){
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; ++test){
		int p,q;
		scanf("%d/%d",&p,&q);
		double r = double(p) / double(q);
		int ret = 1;
		for(int c = 0; c < 40; ++c){
			r *= 2;
			if(r < 1.0) ++ret;
		}
		if((r - floor(r)) != 0.0) printf("Case #%d: impossible\n", test);
		else printf("Case #%d: %d\n", test,ret);
	}
	return 0;
}
