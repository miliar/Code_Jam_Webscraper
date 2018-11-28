#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main(){
int iter;
cin >> iter;
int iterr=0;
while(++iterr <= iter){
		double c,f,goal;
		cin >> c >> f >> goal;
		double x = goal;
		double t = goal/2.0;
		double rate = 2.0;
		double ct =0.0;
		//double ratestart = ct;
		while((x/rate)>(c/rate+(x)/(rate+f))){
			ct += c/rate;
			/*
			//ratestart = ct;
			cout << ct << " , " << rate << " -> " << (x/rate)  << ":" << (c/rate+(x-c)/(rate+f)) <<
						'\t' << ct+x/rate << endl;
			*/
			rate += f;
		}
		t = ct+x/rate;

		cout.precision(14 +(int)log10(t));
		cout << "Case #" << iterr <<": " << t << endl;
}
getchar();

return 0;
}
