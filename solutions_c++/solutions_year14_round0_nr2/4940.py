#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,i=1;
	cin >> t;
	while (t--){
		double C,F,X,total=0.0;
		double rate=2.0;
		cin>>C>>F>>X;
		
		//calculo
		while ((X/rate) > ((C/rate)+(X/(rate+F)))){
			total += (C/rate);
			rate+=F;
		}
		total += (X/(rate));
		
		cout << "Case #"<<i<<": ";
		printf("%.7f",total);
		cout<<endl;
		i++;
	}
	return 0;
}