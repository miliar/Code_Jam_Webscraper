#include<stdio.h>
#include<iostream>

using namespace std;


int main() {
		
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	cin>>T;
	for( int ii = 1; ii <= T; ++ii) {
		int a;
		int sel[17];
		for( int j = 0 ; j <= 16; ++j)
			sel[j] = 0;
		for( int w = 0; w < 2; ++w) {
			cin>>a;
			for( int i = 1; i <= 4; ++i)
				for( int j = 0; j < 4; ++j) {
					int x;
					cin>>x;
					if( i == a) 
						sel[x]++;
				}
		}
		int count = 0, sol;
		for( int i = 1; i <= 16; ++i)
			if( sel[i] == 2) {
				sol = i;
				count++;
			}
		cout<<"Case #"<<ii<<": ";
		if( count == 1) {
			cout<<sol<<endl;
		}
		if( count > 1) {
			cout<<"Bad magician!"<<endl;
		}
		if( count == 0) {
			cout<<"Volunteer cheated!"<<endl;
		}
	}
	return 0;
}
