#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;


int palindrom ( long long num ){

	int a[20];
	int count = 0;

	while ( num != 0 ) {
		int x = num%10;
		a[count]=x;
		count++;
		num=num/10;
	}

	int i ;
	int flg = 1;
	for ( i = 0 ; i < count/2 && flg==1 ; i++ )
		if ( a[i] != a[count-1-i] ) flg = 0;

	return flg; 	
}

int Count ( long long a , long long b) {

	long long i ;
	int num = 0;
	for ( i = a ; i <= b ; i++ ) {
		int tmp = palindrom(i);
		if ( tmp == 1 ) num+=palindrom(i*i); 
	}
	return num;
}

void Readata(){

	ifstream fin("C.in");
	int T;
	fin >> T;
	
	int i;
	for ( i = 1 ; i <= T ; i++ ) {

		long long A , B;
		fin >> A >> B ;

		int a = ceil(sqrt(A));
		int b = sqrt(B);

		cout << Count(a,b) << endl;
	}
}
int main()
{
	Readata();
	return 0;
}
