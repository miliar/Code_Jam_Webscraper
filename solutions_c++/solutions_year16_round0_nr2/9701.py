#include <cstdio>
#include <cstring>
#include <iostream>

int main(){
	using namespace std;

	freopen("B-large.in","r", stdin);
	//freopen("B-large.out","w", stdout);

	int n, sol;
	string cad, d;

	scanf("%d\n", &n);

	for(int i=0;i<n;i++){
		d="";
		getline (cin, cad);
		for( int j=0;j<cad.length();j++){
			if( d=="") d+=cad[j];
			else{
				if( d[d.length()-1]!=cad[j] )
					d+=cad[j];
			}
		}

		sol=d.length()-1;
		while(d[sol]=='+' && sol>=0 ){
			sol--;
		}
		printf("Case #%d: %d\n", i+1,sol+1 );

	}

	return 0;
}

