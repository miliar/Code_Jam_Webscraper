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

int solve(int x, int a, int b){
		int f = -1;
		if(a>b) swap(a, b);
		if(x==1) f = 1;
		else if(a*b%x) f = 0;
		else if(x==2) f = 1;
		else if(a*b==x) f = 0;
		else if(x>=7) f = 0;
		else if(x>b) f = 0;
		else if(x>=2*a+1) f = 0;
		else if(x>=a+b-1) f = 0;
		else if(x==3) f = 1;
		else if(x==4 && a==2) f = 0;
		
		return f;
}
void test(int X, int A, int B){
	for(int i = 1; i <= X; i++){
		printf("X = %d\n", i);
		for(int j = 1; j <= A; j++){
			for(int k = 1; k <=B; k++){
				int r = solve(i, j, k);
				printf("%c", r==1?'o':(r==0?'x':'-'));
			}
			puts("");
		}
	}
}

int main(){
	//test(7, 20, 20);
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int x, a, b;
		cin>>x>>a>>b;
		printf("Case #%d: %s\n", Case, solve(x, a, b)?"GABRIEL":"RICHARD");
	}
	return 0;
}

