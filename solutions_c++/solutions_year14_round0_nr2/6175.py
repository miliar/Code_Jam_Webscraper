#include <iostream>
#include <fstream>
using namespace std;

int main() {
    std::ifstream input("input");
	int T, i, t, j;
	double ans, C, F, X, ans2;
	input >> T;
	for (i=0; i<T; i++)
	{
		t = 0; ans =0; ans2 = 0;
		input >> C >> F >> X;
		ans = X/2;
		for (j=0; j<t+1; j++)
		{
			ans2 += C/(2+j*F);
		}
		ans2 += X/(2+j*F);
		t=t+1;
		while (ans2 < ans)
		{
			ans = ans2;
			ans2 = 0;
			for (j=0; j<t+1; j++)
			{
				ans2 += C/(2+j*F);
			}
			ans2 += X/(2+j*F);
			t += 1;
		}
		cout.precision(15);
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}
