#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;
typedef pair<bool, int> PBI;
int ans = -1;
void print ( int kase ,  string yes )
{
 	 cout <<"Case #"<<kase<<": ";
	 cout<<yes;
	 cout <<"\n";
 	 return ;
}
double C, F, X;
double eps = 1e-7;
double solve(double curRate) {
	double t = X/curRate;
	double ans  = 0;
	while ((t - X/(curRate+F) - C/curRate) > 0 && (t - X/(curRate+F) - C/curRate) > eps) {
		ans += C/curRate;
		curRate += F;
		t = X/curRate;
		//cout << ans << " "<< curRate << " " << t <<"\n";
	}
	ans += t;
	return ans;
}
int main () {
	int T, kase = 0;; 
	for (cin >> T; T; T--) {
		cin >> C >> F >> X;
		cout <<"Case #"<<++kase<<": ";
		printf("%.7f\n", solve(2.0));
	}
	return 0;
}
