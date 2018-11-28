#include <iostream>
#include <fstream>
using namespace std;

long long getLast(long long N) 
{
	int freqs[10] = {0};
	int remDig = 10;
	long long sum = 0;

	while(remDig) 
	{
		sum += N;

		long long tempSum = sum;
		while(tempSum > 0) {
			int d = tempSum%10;
			if (freqs[d] == 0) {
				remDig--;
				freqs[d] = 1;
			}
			tempSum /= 10;
		}		
	}

	return sum;
}


int main()
{
	ifstream cin("A-large.in");
	ofstream cout("Counting_Sheep_Sevag_Large.out");

	int N, T;

	cin>>T;

	for (int t=1; t<=T; t++)
	{
		cin>>N;
		if (N==0){
			cout<<"Case #"<<t<<": INSOMNIA"<<endl;
		}else {
			cout<<"Case #"<<t<<": "<<getLast(N)<<endl;
		}
	}

	return 0;
}