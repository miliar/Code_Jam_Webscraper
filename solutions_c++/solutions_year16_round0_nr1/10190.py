#include<bits/stdc++.h>

using namespace std;

int func( int n ){
	int x, i = 1, count = 0; 
	bool seen[10] = {false};
	while( true ){
		x = i*n;
		//cout << count << endl;
		while( x > 9 ){
			if( !seen[x%10] ){
				count++;
				seen[x%10] = true;
			}
			if( count == 10 )
				break;
			x = ( x - (x%10) )/10;
		}
		if( x <= 9 )
			if( !seen[x] ){
				count++;
				seen[x] = true;
			}
		if( count == 10 )
			break;
		i++;
	}
	return i*n;
}

int main(){
	int t;
	ofstream myfile;
  	myfile.open ("salida.out");
  	string salida;
	scanf(" %d", &t);
	for( int i = 1; i <= t; i++ ){
		int n;
		scanf(" %d", &n);
		if( n != 0 ){
			myfile << "Case #" << i  << ": " << func( n ) << "\n";
		}else{
			myfile << "Case #" << i  << ": INSOMNIA\n";
		}
		
	}
	myfile.close();
}
