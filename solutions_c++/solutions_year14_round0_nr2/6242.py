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
#include <iomanip>
using namespace std;


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
	
    int t2;
    cin >> t2;
	double C,F,X;
	double sum=0;
	double Nd=0;
	int N=0;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        cin >> C>>F>>X;
		Nd=(X/C)-(2/F);
		if(Nd<1)N=1;
		else N=int(Nd+1);
		sum=0;
		for( int i=0;i<N-1;++i)
		{
			sum+=C/(2+i*F);
		}
		sum+=X/(2+(N-1)*F);
		cout<<fixed <<setprecision(7) << sum;
        printf("\n");
    }
    
    return 0;
}
