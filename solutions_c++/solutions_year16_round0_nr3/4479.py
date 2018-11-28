#include<iostream>
#include<cstring>
#include<string>
#include<bitset>
using namespace std;
long long N, J, T;


long long pow[20][20]; //system, x^..
int t[20];
int main(){
	cin >> T >> N >> J;
	cout << "Case #1:" << endl;
	long long m = 1 << 15;
	long long m0 = 0;
	for (int k = 2; k <= 10; ++k) {
		pow[k][0]=1;
		for (int i = 1; i < 17; ++i) pow[k][i] = pow[k][i-1]*k;
	};
/*	for (long long i = m0; i < m; ++i) {
		long long x = 1 << 15;
	        //x += i;	
		x = x << 1; x += 1;
		bitset<16> b(x);
		cout << x << " " << b << endl;
		
	};*/
	t[0]=1;  t[15]=1;
	int ret=0;
	for (t[14]=0; t[14] <=1; t[14]++){
	for (t[13]=0; t[13] <=1; t[13]++){
	for (t[12]=0; t[12] <=1; t[12]++){
	for (t[11]=0; t[11] <=1; t[11]++){
	for (t[10]=0; t[10] <=1; t[10]++){
	for (t[9]=0; t[9] <=1; t[9]++){
	for (t[8]=0; t[8] <=1; t[8]++){
	for (t[7]=0; t[7] <=1; t[7]++){
	for (t[6]=0; t[6] <=1; t[6]++){
	for (t[5]=0; t[5] <=1; t[5]++){
	for (t[4]=0; t[4] <=1; t[4]++){
	for (t[3]=0; t[3] <=1; t[3]++){
	for (t[2]=0; t[2] <=1; t[2]++){
	for (t[1]=0; t[1] <=1; t[1]++){
/*		for (int i = 15; i >= 0; --i) {
			cout << t[i];
		};*/
		int primecnt = 0;
		int primediv[15];
		long long licz = 0;
		for (int sys = 2; sys <= 10; sys++) {
			licz = 0;
			for (int  i = 0; i <= 16; ++i){
				if (t[i]==1) licz += pow[sys][i];
			};
			bool prime = true;
			if (licz%2==0){ prime=false; primediv[sys]=2;};
			if (prime) {
				for (int z = 3; (z <= 1000 &&  prime); z+=2){
					if (licz%z==0){ prime=false; primediv[sys]=z;};
				};
			};
			if (!prime) primecnt++;
			//cout << " " << licz << (prime?"+":"-");
		};
		//cout << " " << primecnt;
		//cout << endl;
		if (primecnt==9) {
			ret++;
			cout << licz;
			for (int i = 2; i <= 10; ++i) 
				cout << " " << primediv[i];
			cout << endl;
		};
		if (ret==J) return 0;

	};
	};
	};
	};
	};
	};
	};
	};
	};
	};
	};
	};
	};
	};
};
