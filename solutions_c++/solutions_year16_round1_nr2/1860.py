#include <iostream>
using namespace std;
int tab[3000];
int main(){
	int n;
	int t, tmp;
	cin>>t;
	for(int k = 1; k <= t; k++){
		for(int i=0;i<3000;i++)
			tab[i]=0;
		cin >> n;
		for(int i = 0; i < 2 * n - 1; i++){
			for(int j = 0;j<n;j++){
				cin>>tmp;
				tab[tmp] ^= 1;
			}
		}
		cout<<"Case #"<<k<<":";
		for(int i=0;i<3000;i++){
			if(tab[i])
				cout<<" "<<i;
		}
		cout<< endl;
	}
	return 0;
}