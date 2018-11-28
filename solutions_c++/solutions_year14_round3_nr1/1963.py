#include <cstdio>
using namespace std;
#define ll long long

int gcd (int a, int b) {
        if (b == 0)
                return a;
        return gcd (b, a%b);
}

int main() {
        int tcase;
        scanf ("%d", &tcase);
        for (int num = 1; num <= tcase; num ++) {
                ll P, Q;
                scanf ("%lld/%lld", &P, &Q);
                printf ("Case #%d: ", num);
                if (Q == 1) {
                        printf ("0\n");
                        continue;
                }
                int gcdVal = gcd (Q, P);
                P /= gcdVal;
                Q /= gcdVal;

                if (Q%2 || P>Q)
                {
                        printf ("impossible\n");
                        continue;
                }
                
		bool flag = false;
                ll temp_q = Q;
                while (temp_q > 1) {
			if (temp_q&1) {
				flag = true;
				break;
			}
                        temp_q = temp_q >> 1;
                }
		
                if (flag)
                	printf ("impossible\n");
                else
		{
	                int cnt = 0;
                	while (P < Q)
	                {
        	            Q = Q >> 1;
                	    cnt ++;
                	}
	                printf ("%d\n", cnt);
		}
        }
        return 0;
}
