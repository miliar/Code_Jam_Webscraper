#include <iostream>
#include <cstdio>
#include <set>


using namespace std;

int main()
{
	int T;
	scanf("%d", &T);

	for (int c = 1; c <= T; ++c) {
		
		double C, F, X;

		scanf("%lf %lf %lf", &C, &F, &X);


		/*
			t[0] = X / 2
			t[1] = X / (2 + F) + C / 2
			t[2] = X / (2 + 2F) + C / (2 + F) + C / 2
			t[n] = X / ((2 + n * F)) +  SUM (C / (2 + (n - 1)* F),n = 1...)
		*/
		double p = 2;
		double t_acc = 0;
		double t = 0;
		double t_ant = 0;
		int n = 0;


		while (true) {
			if (n == 0) {
				t = X / 2;
				t_acc = C / 2;
			} else {
				t = X / (2 + n * F) + t_acc;
				t_acc += C / (2 +  n * F);
			}

			if (t > t_ant and n > 0) {
				t =  t_ant;
				break;
			} else {
				t_ant = t;
			}
			++n;
			
		}

		printf("Case #%d: %.7lf\n", c, t);
		
	}

	return 0;
}


