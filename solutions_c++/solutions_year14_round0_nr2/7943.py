#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int t, i;
	double m = 0;
	double c, f, x;
	int k = 0;
	cin >> t;
	while(t--){
	    k++;
	    i = 1;
		scanf("%lf%lf%lf",&c,&f,&x);
        double time = 0, hug = 0;
        time += c/2.0;
        m =  x/(2.0+i*f);

        while(1){
            hug +=  c/(2.0+i*f) + x/(2.0+(i+1)*f);
            if(m < hug) break;
            else{
                m = hug;
                hug -= x/(2.0+(i+1)*f);
            }
            ++i;
        }
			printf("Case #%d: %.6f\n", k, min((m+time),x/2.0));
    }
	return 0;
}
