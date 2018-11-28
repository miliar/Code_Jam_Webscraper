#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long int test;
	cin>>test;
	for(long long int i=1;i<=test;i++){
		double c,f,x;
		double rate,rate1,init,fin,res;
        	rate = 2.0;
                cin >> c >> f >> x;
                res = x/rate;
                rate1 = f + 2.0;
                init = c/rate;
                fin = init + c/rate1;
                rate = rate + f;
                rate1 = rate1 + f;
                while((init + x/rate)>(fin + x/rate1)){
                	init = init + c/rate;
                	fin = fin + c/rate1;
                	rate+=f;
                	rate1+=f;
                }
                printf("Case #%lld: ",i);
                printf("%.7lf\n",min(res,init + x/rate));
       }
    return 0;
}
