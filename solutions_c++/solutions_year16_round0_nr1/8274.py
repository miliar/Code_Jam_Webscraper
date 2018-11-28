#include<iostream>
#include<string.h>
#include<fstream>
#define LL long long
using namespace std;

ofstream coutf; 
int main()	{
	coutf.open("output.txt");
	LL check = (1 << 11) - 1;
	int N;
	LL tmp;
	int t, T;
	cin >> T;
	for (t = 0; t < T; t++){
		check = (1 << 10) - 1;
		cin >> N;
		if (N == 0){
			coutf << "Case #" <<t+1<< ": ";
			coutf << "INSOMNIA" << '\n';
			continue;
			}
		tmp = N;
		LL rst = 0;
		for (int i = 1; i ; i++){
			tmp = N*i;

			while (tmp){
				LL dlt = tmp % 10;
				if (check & (1 << dlt))
					check &= ~(1 << dlt);
				tmp /= 10;
			}

			if (check == 0){
				rst = N*i;
				break;
			}
		}
		
		coutf <<"Case #"<< t + 1 <<": ";
		coutf << rst << '\n';

	}


	return 0;
}