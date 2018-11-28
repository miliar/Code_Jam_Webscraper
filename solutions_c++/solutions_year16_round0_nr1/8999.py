#include <iostream>
using namespace std;


int calculate (int x){
	int sum = 0, i = 1, digit;
	if (x==0)
		return 0;
	int val[10];
	int j;
	for (j=0; j<10; j++){
		val[j]=0;
	}
	while (1){
		int temp = i*x;

			while (temp!=0){
				digit = temp%10;
				temp = temp/10;

	//			cout <<"digit = "<<digit <<"temp ="<< temp<<endl;

				if (val[digit]==0){
					val[digit]=1;
					sum = sum + 1;
				}
				

			}
				if (sum==10)
					break;

	//cout <<"sum ="<<sum << "i = " <<i <<endl;				
	i++;

	}
	return i*x;	
}



int main () {
	int test, ans, x, i;
	cin >> test;

	for (i=0; i<test; i++){
		cin >> x;
		ans = calculate(x);
		if (ans==0)
			cout <<"Case #"<<i+1<<": INSOMNIA"<<endl;
		else
			cout <<"Case #"<<i+1<<": "<<ans<<endl;

	}
}