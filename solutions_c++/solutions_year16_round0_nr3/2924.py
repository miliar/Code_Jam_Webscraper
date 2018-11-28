#include <iostream>
using namespace std;

int jam[100];
int found = 0;
int N, T, J;

long long pw(int x, int y){
	long long numb = 1;
	for (int t = 0; t < y; t++){
		numb*=x;
	}
	return numb;
}

int check(){
	//Base you interpret it in
	int fail = 0;
	int factor[10];
	for(int b = 2; b<=10; b++){
		unsigned long long num=0;
		for (int a = 1; a<=N; a++){
			num += jam[a]*pw(b,(N-a));
		}
		
		//cout << "Base " << b << " checking " << num << " ";
		//for (int a=1;a<=N; a++) cout << jam[a];
		//cout << endl;
		//Interpret the number first in base 10
		
		//Check if it's prime
		int prime = 1;
		for(int a = 2; a*a<=num; a++){
			if(num%a==0){
				prime = 0;
				factor[b] = a;
				break;
			} 
		}
		
		//If it's prime, this fails
		if(prime == 1) fail++;
	}
	if (fail==0){
		if(found<J){
			for (int a = 1; a<=N; a++) cout << jam[a];
			for (int a = 2; a<=10; a++) cout << " " << factor[a];
			cout << "\n";
		}
		found++;
	}
}

int rec(int x){
	
	if(found<J){
	
	
		if(x==N){
			check();
		}
		else{
			jam[x]=0;
			rec(x+1);
			jam[x]=1;
			rec(x+1);	
		}
		
	}
}

int main(){
	cin >> T >> N >> J;
	cout << "Case #1:\n";
	//First and last must be 1
	jam[1]=1;	
	jam[N]=1;
	rec(2);
	
	return 0;
}
