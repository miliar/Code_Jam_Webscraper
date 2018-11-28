#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
using namespace std;

string cad;
int A[2000], B[2000], mx, md;

int valido(int md){
	B[0]=A[0]+md;
	for( int i = 1; i<cad.length();i++  ){
		if( B[i-1]>=i ) B[i] = B[i-1]+cad[i]-'0';
		else return 0;
	}
	return 1;
}

int solucion(const string &cad){
	int lo, hi, sol;
	A[0]=cad[0]-'0';
	mx = cad.length()-1-A[0];
	
	if(mx<=0) return 0;
	lo = 0, hi = mx;
	for( int i=1;i<cad.length();i++ ){
		if( A[i-1]>=i ) A[i] = A[i-1] + cad[i] - '0';
		else A[i] = 0;
	}
	
	sol=mx;
	while( lo<=hi ){
		md = (lo+hi)/2;
		if( valido(md) ){
			if( sol>md )
				sol=md;
			hi = md-1;
		}
		else lo = md+1;
	}
	
	return sol;
	
}

int main() {
	int n, T;
	scanf("%d\n", &T);
	for( int i=0;i<T;i++){
		cin>>n>>cad;
		cout<<"Case # "<<i+1<<": "<< solucion(cad)<<'\n';
		cad.clear();
	}
	return 0;
}