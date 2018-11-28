using namespace std;
#include <iostream>
#include <cstdio>
#include <string>

#define INF 1000000000000000

int main(){
	int t;
	double c, f, x, cpms;
	double acm, best;

	cin >> t;
	
	for(int l = 1;l <= t;l++){
		acm = 0; best = INF;	
		cpms = 0.2;

		cin >> c >> f >> x;
		f /= 10;

		while(1){
			if(acm+x/cpms < best){
				best = acm+x/cpms;
				
				acm += c/cpms;
				cpms += f;
			}
			else{
				break;
			}
		}

		best /= 10;
		cout << "Case #" << l << ": ";
		printf("%.7lf\n", best);

	}

	return 0;
}
