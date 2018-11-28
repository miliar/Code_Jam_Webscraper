#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>
#include <iomanip>

#define re
using namespace std;


int t;
double c,f,x;

double solve(double rate){

	double r1 = x/rate;
	double r2 = c/rate + x/(rate+f);
	if(r1>r2)
		return c/rate + solve(rate+f);
	else 
		return r1;


}


int main(int argc, char const *argv[])
{
#ifdef re
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
freopen("log.txt","w",stderr);
#endif

cin>>t;
for(int i=1;i<=t;i++){
	cin>>c>>f>>x;
	cout<<"Case #"<<i<<": "<<std::setprecision(7)<<fixed<<solve(2)<<endl;
}
    	
/*#ifdef re
printf("\n  Time Taken  %.31f sec\n",(double)clock()/(CLOCKS_PER_SEC));

#endif*/
return 0;
}
