#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("infile.txt", "r", stdin);
	freopen("outfile.txt", "w", stdout);
	int t;
	
	cin >> t;
	for (int s = 1; s <= t; s++) {
		double c, f, x;
		double time = 0, sp = 2;
		
		cin >> c >> f >> x;
		
		if (x < c) {
			//cout.precision(7);
			//cout << x / sp << endl;
			printf("Case #%d: %.7lf\n", s, x / sp);
			continue;
		}
		
		
		while (1){
			double t1, t2;
			
			t1 = (x - c) / sp;
			t2 = x / (sp + f);
			
			time += c / sp;
			if (t1 < t2) {
				time += t1;
				break;
			} else {
				sp += f;
			}
		} 
		
		//cout.precision(20);
		//cout << time << endl;
		printf("Case #%d: %.7lf\n", s, time);
	}
}
