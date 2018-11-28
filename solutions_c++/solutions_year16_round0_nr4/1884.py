#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main(){
	int cases;
	cin >> cases;
	int k, c, s;
	for( int i=0; i<cases; i++){
		cin >> k >> c >> s;
		printf("Case #%i: ", i+1);
		for( int i=1; i<=k; i++) printf("%i ", i);
		printf("\n");
	}
	return 0;
}
