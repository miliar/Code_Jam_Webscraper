#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

long long int pot[19];

int k_ta(long long int m, int k){
	int l = 1; 
	while(k > 0){
	l = l * 10;
	k--;}
	m = m / l;
	return m % 10;
}

int zamien(string S){
	int k = 0;
	int wart = 0;
	
	for(int l = S.size() - 1; l >= 0; l--){
		wart = wart + (S[l] - '0') * pot[k];
		k++;
	}
	return wart;
}

int main(){
	ios_base::sync_with_stdio(false);
	int z;
	cin >> z;
	pot[0]=1;
	for(int p=1; p <=18; p++)
		pot[p] = pot[p-1]*10;
	for(int ll = 1; ll <= z; ll++){
		
		string A, B;
		
		cin >> A >> B;
		
		int abs_min = 1000000;
		string resA, resB;
		int walA = -1, walB=-1;
		int PP=1;
		X:;
		if(A.size() == 1){
			for(int i = 0; i <= 99; i++){
				string newA = A, newB = B;
				if(A[0] == '?')
					newA[0] = (char)(k_ta(i, 1) + '0');
				if(B[0] == '?')
					newB[0] = (char)(k_ta(i, 0) + '0');
				int wart = zamien(newA);
				int wart2 = zamien(newB);
				
				int mins = abs(wart-wart2);
				if(mins == abs_min && walA == wart){
					if(walB > wart2){
					abs_min = mins;
					resA = newA;
					resB = newB;
					walA = wart;
					walB = wart2;
					}
				}
				
				if(mins == abs_min && walA > wart){
					abs_min = mins;
					resA = newA;
					resB = newB;
					walA = wart;
					walB = wart2;
				}
				if(mins < abs_min){
					abs_min = mins;
					resA = newA;
					resB = newB;
					walA = wart;
					walB = wart2;
				}
				
				
				
			}
		}
		if(A.size() == 2){
			for(int i = 0; i <= 9999; i++){
				string newA = A, newB = B;
				if(A[0] == '?')
					newA[0] = (char)(k_ta(i, 2) + '0');
				if(A[1] == '?')
					newA[1] = (char)(k_ta(i, 3) + '0');
				if(B[0] == '?')
					newB[0] = (char)(k_ta(i, 0) + '0');
				if(B[1] == '?')
					newB[1] = (char)(k_ta(i, 1) + '0');	
				int wart = zamien(newA);
				int wart2 = zamien(newB);
				
				int mins = abs(wart-wart2);
				
				if(mins == abs_min && walA == wart){
					if(walB > wart2){
					abs_min = mins;
					resA = newA;
					resB = newB;
					walA = wart;
					walB = wart2;
					}
				}
				
				if(mins == abs_min && walA > wart){
					abs_min = mins;
					resA = newA;
					resB = newB;
					walA = wart;
					walB = wart2;
				}
				if(mins < abs_min){
					abs_min = mins;
					resA = newA;
					resB = newB;
					walA = wart;
					walB = wart2;
				}
			}
		}
		
		if(A.size() == 3){
			for(int i = 0; i <= 999999; i++){
				string newA = A, newB = B;
				if(A[0] == '?')
					newA[0] = (char)(k_ta(i, 3) + '0');
				if(A[1] == '?')
					newA[1] = (char)(k_ta(i, 4) + '0');
				if(A[2] == '?')
					newA[2] = (char)(k_ta(i, 5) + '0');
				if(B[0] == '?')
					newB[0] = (char)(k_ta(i, 0) + '0');
				if(B[1] == '?')
					newB[1] = (char)(k_ta(i, 1) + '0');	
				if(B[2] == '?')
					newB[2] = (char)(k_ta(i, 2) + '0');	
				int wart = zamien(newA);
				int wart2 = zamien(newB);
				
				
				int mins = abs(wart-wart2);
				
			if(mins == abs_min && walA == wart){
					if(walB > wart2){
					abs_min = mins;
					resA = newA;
					resB = newB;
					walA = wart;
					walB = wart2;
					}
				}
				
				if(mins == abs_min && walA > wart){
					abs_min = mins;
					resA = newA;
					resB = newB;
					walA = wart;
					walB = wart2;
				}
				if(mins < abs_min){
					abs_min = mins;
					resA = newA;
					resB = newB;
					walA = wart;
					walB = wart2;
				}
			}
		}
		
		if(PP==1){
			PP=2;
		goto X;
	}
		cout << "Case #" << ll << ": ";
		
		cout << resA << " " << resB << endl;
		
	}
}
