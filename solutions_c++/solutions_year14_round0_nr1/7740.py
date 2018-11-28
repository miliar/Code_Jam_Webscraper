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
		int first, second;
		vector<int> f, s;
		scanf("%d", &first);
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				int temp;
				scanf("\n%d", &temp);
				if(i == first - 1){
					f.push_back(temp);
				}
			}
		}
		scanf("%d", &second);
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				int temp;
				scanf("\n%d", &temp);
				if(i == second - 1) s.push_back(temp);
			}
		}
		int count = 0, val = f[0];
		for(int i = 0; i < f.size(); ++i){
			for(int j = 0; j < s.size(); ++j){
				if(f[i] == s[j]) {
					++count;
					val = f[i];
				}
			}
		}
		if(count == 1) printf("Case #%d: %d\n", test,val);
		else if(count > 1) printf("Case #%d: Bad magician!\n",test);
		else if(count == 0) printf("Case #%d: Volunteer cheated!\n",test);
	}
	return 0;
}
