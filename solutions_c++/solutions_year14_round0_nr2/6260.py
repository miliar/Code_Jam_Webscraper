#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
const int N = 100010;
const LL MOD = 1000000007;

int main(){

	freopen("0.in", "r", stdin); 
	freopen("out.txt", "w", stdout);
	int T, x, y,tmp;
	cin >> T;
	for (int t = 1; t <= T; t++){
		double c, f, x;
		cin >> c >> f >> x;
		double tt = 0;
		double r = 2.0f;
		while (1){
			double pt = x / r;
			double xt = c / r + x / (r + f);
			if (xt < pt){
				tt += c / r;
				r = r + f;
			}
			else{
				tt += pt;
				break;
			}
		}

		printf("Case #%d: ",t);
		printf("%.7lf\n", tt);
	}
}