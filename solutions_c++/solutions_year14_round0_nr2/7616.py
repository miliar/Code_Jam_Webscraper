#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <cmath>
#include <ctime>
using namespace std;
 
#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
typedef vector<int> VI;
typedef pair<int,int> pII;
typedef vector<string> VS;
typedef long long LL;

double eps = (double)1e-9;

int main() {
	int T;
	cin >> T;
  
	for(int t = 1; t <= T; t ++) {
		cout << "Case #" << t << ": ";
	
		double C, F, X;
		cin >> C >> F >> X;
		
		double S = 2.0;
		double sumA = 0.0;
		vector<double> sec;
		
		double ret = 0.0;		
		while(true) {
			double a = C / S;
			double b = X / S;
			double c = X / (S + F);
			if(b < a + c) {
				ret += b;
				break;
			}
			else
				ret += a;
			S += F;
		}

		printf("%.7lf\n", ret);
	}

	return 0;
}