#include<iostream>
#include<fstream>
#include<string>
#include<cmath>

using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("C-small-attempt0.out");

int T = 0;

bool ispal(int);

int main()
{
	fin >> T;
	int A = 0;
	int B = 0;
	for(int i = 0; i < T; i++){
		fin >> A >> B;
		int a = sqrt(A);
		int b = sqrt(B);
		b++;
		int counter = 0;
		for(int k = a; k < b; k++){
			int K = k*k;
			if(ispal(k) && ispal(K) && K >= A && K <= B){
				counter++;
			}
		}
		fout << "Case #" << i+1 <<": "<< counter;
		if(i < T-1){ fout << endl;}
	}
	return 1;
}

bool ispal(int n)
{
	bool ret = 1;
	int digit[200] = {0};
	if(n < 1) return 0;
	int d = 1;
	digit[0] = n%10;
	while(n/10){
		n = n/10;
		digit[d] = n%10;
		d++;
	}
	for(int i = 0; i < d; i++){
		if(digit[i] != digit[d-i-1]){
			ret = 0;
			break;
		}
	}
	return ret;
}