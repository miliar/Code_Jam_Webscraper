#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main()
{
		freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	vector <double> v;
	double c, f,x, t, a, b;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> c >> f >> x;
		int count = 0;
		v.clear();
		t = 0;
		a = x/2;
		b = t+x/(2+f);
		while(a > b) {
			t = c/(f*count +2);
			a = x/(f*count + 2);
			int tmp = count+1;
			double F = tmp*f;
			b = t + x/(F+2);
			if (a > b) 
	 			v.push_back(t);
			else 
				v.push_back(a);
			count++;
		}
		double sum = 0.0;
		for (int k = 0; k < v.size(); k++) {
			sum += v[k];
		}

		printf("case #%d: %0.7lf\n", i+1,sum);
	}
	return 0;
}
	
