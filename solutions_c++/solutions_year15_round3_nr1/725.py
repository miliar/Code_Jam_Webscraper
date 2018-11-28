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

int R, C, W;

int calc(int C, int W){
	int res = 0;
	while(C>W){
		res++;
		C -= W;
	}
	return res+W;
}


int calc2(int C, int W){
	int res = 0;
	while(C>=W){
		res++;
		C -= W;
	}
	return res;
}

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		cin>>R>>C>>W;
		printf("Case #%d: %d\n", Case, calc(C, W)+(R-1)*calc2(C, W));
	}
	return 0;
}

