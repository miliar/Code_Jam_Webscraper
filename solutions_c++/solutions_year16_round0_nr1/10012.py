
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <algorithm>

using namespace std;


int ProcessInput();
int N, Ntry, k, nDigitSeen, div10, rem10;
int Digits[10];

int main()
{

	int testcases, i;

	cin >> testcases;

	for(i=0; i < testcases; i++) {
		cout<<"Case #"<<i + 1<<": ";
		ProcessInput();
	}

return 0;
}

 
int ProcessInput()
{
cin >> N;

if(N==0)
	cout<<"INSOMNIA"<<endl;
else {
	nDigitSeen = 0;
	for(int i=0; i < 10; i ++)
		Digits[i] = 0;
	Ntry = 0;
	while(1) {
	Ntry += N;
	k = Ntry;
	while(k!=0) {
		div10 = k/10;
		rem10 = k - 10*div10;
		if(Digits[rem10]==0) {
			Digits[rem10] ++;
			nDigitSeen ++;
			if(nDigitSeen == 10) {
				cout<<Ntry << endl;
				return 0;
			}
		}
		k = div10;
	}
	}
}

return 0; 
}

