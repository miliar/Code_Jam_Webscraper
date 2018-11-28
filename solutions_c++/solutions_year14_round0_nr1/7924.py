#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

int T;
int carte[4][4];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	for(int i=0; i< T; i++) {
		int primo, secondo;
		vector< int >possib;
		cin >> primo;
		for(int j=0; j < 4; j++)
		  for(int k=0; k < 4; k++) cin >> carte[j][k];
		
		for(int j=0; j < 4; j++) possib.push_back(carte[primo-1][j]);
		
		cin >> secondo;
		int c=0, carta=0;
		
		for(int j=0; j < 4; j++)
		  for(int k=0; k < 4; k++) cin >> carte[j][k];
		
		for(int j=0; j < 4; j++) {
			for(vector< int >::iterator h = possib.begin(); h != possib.end(); h++) 
			    if(*h == carte[secondo-1][j]) { c++; carta = carte[secondo-1][j]; }
			
			if(c > 1) break;
		}
		cout<<"Case #"<<i+1<<": ";
		if(c > 1)cout<<"Bad magician!\n";
		else if(c == 1) cout<<carta<<endl;
		else cout<<"Volunteer cheated!\n";
		
	}
	
}
