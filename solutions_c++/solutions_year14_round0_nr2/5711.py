#include <iostream>
#include <iomanip>
#include <string.h>
using namespace std;
int main() {
	int test=0;
	cin>>test;
	int test_case=1;
	while(test--){
		double C,F,X;
		cin>>C;
		cin>>F;
		cin>>X;
		int max_entry=X/C+1;
		double *table=(double *)malloc(sizeof(double)*(max_entry));
		memset(table,0,sizeof(double)*max_entry);
		double rate=2;
		double first_farm_buy_time=C/2;
		table[0]=X/2;
		int i=1;
		while(true){
			double calc=first_farm_buy_time+(X/(rate+F));
			double min=table[i-1]<calc?table[i-1]:calc;
			if(min < calc){
				cout<<"Case #"<<test_case<<": "<<std::setprecision(10)<<min<<endl;
				//cout<<"Case #"<<test_case<<": "<<min<<endl;
				test_case++;
				break;
			}
			table[i]=min;
			i++;
			rate=rate+F;
			first_farm_buy_time+=C/(rate);
		}
		free(table);
		table=NULL;
	}
	return 0;
}