#include <iostream>
using namespace std;

int main() {
	int tab[2502];
	for(int i = 0; i < 2502; i++) tab[i]=0;
	int T, N;
	int height, counter;
	
	cin>>T;
	
	for(int i = 1; i <= T; i++) {
		cin>>N;
		for(int j = 0; j < (2*N)-1; j++) {
			for(int x = 0; x < N; x++) {
				cin>>height;
				tab[height]++;
			}
		}
		counter = 0;
		
		cout<<"Case #"<<i<<": ";
		for(int j = 0; j < 2502; j++) {
			if( tab[j]%2 == 1) {
				counter++;
				cout<<j;
				if(counter != N) cout<<" ";
			}
		}
		cout<<endl;
		if(counter != N) cout<<"CABOOM!!\n";
		for(int i = 0; i < 2502; i++) tab[i]=0;
	}
}
