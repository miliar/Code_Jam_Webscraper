#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    freopen("dataset", "r", stdin);
    freopen("output", "w", stdout);

    int t;
    cin >> t;
    for (int t1 = 1; t1 <= t; ++t1) {
        printf("Case #%d: ", t1);
        double c, f, x;
        cin >> c >> f >> x;

		double total_time = x/2;
		double time_farm = 0;
			
		for(int nf=1; true; nf++){

			time_farm += c/(f*(nf-1)+2);
			double tempo = x/(f*nf+2) + time_farm;
			
			if(tempo < total_time)
				total_time = tempo;
			else{
				if (tempo > total_time)
					break;
				}
		}

		printf("%.*lf\n",7,total_time);
    }
    
    return 0;
}
