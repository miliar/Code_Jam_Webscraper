#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<set>

using namespace std;

int main(){
	int t, count = 1, n;
	double c, f, x, y, ct;
	double eps = 1e-10;
	
	cin >> t;
	while(t--){
		cin >> c >> f >> x;
		
		n = 0;
		ct = 0;
		y = x/2.0;
		while(c/(n*f+2) + ct + x/((n+1)*f+2) < y){
			ct += c/(n*f+2);
			n++;
			y = ct + x/(n*f+2);
		}
		
		cout << "Case #"<< count++ << ": ";
		printf("%.7f", y + eps);
		cout << endl;
	}
	
	return 0;
}

