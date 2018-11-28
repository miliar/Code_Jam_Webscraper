#include<bits/stdc++.h>

using namespace std;
float const ep = 1e6;

int main(){
	freopen("B-large.in","r", stdin);
	freopen("outputB.out","w",stdout);
	int t;
	double c, f, x;
	cin >> t;
	for (int k = 1; k <= t; k++){
		cin >> c >> f >> x;
		double d = 2, res = 0;
		while(true){
			double r1 = (double)  (x/d);
			double r2 = (double) (c/d + x/ (d+f));
			if (r1 - r2 < 0) break;
			double t1 = (double)(c/d);
			res += (double) t1;
			d += f;
		}
		res += (double) x/d;
		cout << "Case #" << k << ": ";
		printf("%0.7f",(double) res);
		cout << endl;
			
		
	}
}
