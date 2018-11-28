
#include <cstdio>
#include <iostream>
#include <string.h>
#include <cmath>

using namespace std;
long long v[50];
long long  res[15];

long long isPrime(long long n){
	long long res = 0;
	for (long long i = 2; i <= sqrt(n); ++i){
		if(n % i == 0){
			res = i;
			return res;
		}
	}
	return res;
	
}

bool getBinary(long long len, long long n){
	memset(v,sizeof v, 0);
	v[0] = 1;
	v[len-1] = 1;
	string cad = "";
	long long pos = len-1,mask = n;
	while(mask >0){
		if((mask & 1) == 1){
			//v[pos] = 1;
			cad = '1' + cad; 
			//cout << 1 ;
		} else {
			//v[pos] = 0;
			// cout << 0 ;
			 cad = '0' + cad; 
		}
    	pos --;
    	mask >>= 1;	
	}
	pos = len-2;
	if(n != 0 ){
		for (long long i = cad.size() -1 ; i >= 0 ; --i){
			if(cad[i] == '1'){
				v[pos] = 1;
			} else {
				v[pos] = 0;
			}
			pos --;
		}
	}
	string cad2 = "";
	// cout << cad << endl;
	for (long long i = 0; i < len; ++i){
		cad2 = cad2 + (char)(v[i]+48);
		/* code */
	}
	//cout << cad2 << endl;
	// cout << endl;
	// //cout <<endl;
	bool acc = true;
	for (long long i = 2; i <= 10; ++i){
		long long resu = 0;
		long long p = 1;
		for (long long j = len-1; j >= 0; --j){
			resu = resu + (p* v[j]);
			p = p * i;
		}
		 // cout << resu << endl;
		long long d = isPrime(resu);
		if(d != 0){
			res[i] = d;
		} else {
			acc = false;
		}
	}
	if(acc ){
		cout << cad2 << " ";
		for (long long i = 2; i <= 10; ++i){
			if(i == 10){
				cout << res[i] ;
			} else {
				cout << res[i] << " ";
			}
		
		}
		cout << "\n";
		return true;
	} 
	return false;
}

void getJamCoins(long long len, long long n){
	for( long long i = 0 ; i < ( 1 << (len-2)) ; ++ i ) {   
		
		if(getBinary(len,i)){
			n--;
		}
		if(n == 0){
			break;
		}

	}
}
int main(){
	long long t,min,len;
	  freopen("c.in","r",stdin);
	  freopen("C-small-attempt1.out","w",stdout);
	cin >> t; 
	for (long long i = 1; i <= t; ++i){

		cin >> len >> min;
		long long y = 0;
		cout << "Case #1:"<< endl;
		getJamCoins(len,min);
		//printf("Case #%d: %d\n", i,y);	
	}
	return 0; 
}