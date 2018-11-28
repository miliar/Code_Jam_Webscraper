#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		double c, f, x;
		cin >> c >> f >> x;
	
		double ans = x/2.0;
		double per = 2.0;
		double time = 0.0;
		while (1) {
			time += c/per;
			per += f;
			
			if (time + x/per < ans)
				ans = time + x/per;
			else
				break;
		}
		printf("Case #%d: %.7f\n", i+1, ans);
	}
	return 0;
}