#include <cstdio>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int n;
	cin>>n;
	for(int i=1; i<=n; i++){
		double C, F, X;
		cin>>C>>F>>X;
		double rate=2;
		double time=0;
		while(((double)X/rate) > (((double)C/rate) + (X/(double)(rate+F)))){
			time += C/rate;
			rate += F;
		}
		time += X/rate;
		printf("Case #%d: %.7lf\n", i, time);
	}
	return 0;
}