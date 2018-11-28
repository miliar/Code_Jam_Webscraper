#include <iostream>
#include <cstdio>
using namespace std;

int main () {
	freopen("B-large.in","r", stdin);
	freopen("out.txt","w",stdout);
	
	int N;
	cin >> N;
	for(int n=1; n<=N; n++) {
		double c, f, x;
		cin >> c >> f >> x;
		
		double F = 2.00, sec = 0.00;
		while(1) {
			if( (c/F+x/(F+f)) < x/F ) {
				sec += c/F;
				F += f;
			}
			else {
				sec += x/F;
				break;
			}
		}
		
		
		cout << "Case #" << n << ": ";
		printf("%lf\n", sec);
	}
}
