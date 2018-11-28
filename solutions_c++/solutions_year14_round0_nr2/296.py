#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;


int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		double C,F,X;
		cin>>C>>F>>X;
		double R = X/C;
		int r = R;
		double S = 2.0;
		double res2 = 0.0, res = X/S;
		for(int i = 0; i < 100000; i++){
			res2 += C/S;
			S += F;
			res = min(res,res2+X/S);
		}
		printf("Case #%d: %.7lf\n", Case, res);
	}
	return 0;
}

