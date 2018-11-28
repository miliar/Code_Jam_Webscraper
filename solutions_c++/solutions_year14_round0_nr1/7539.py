#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin>>T;
	for(int k=1; k<=T; k++) {
		int a,b;
		vector<vector<int> >v(2,vector<int>(4,0));
		cin>>a;
		for(int i=1;i<=4;i++) {
			for(int j=0;j<4;j++) {
				if (i==a) cin>>v[0][j];
				else cin>>b;
			}
		}
		cin>>a;
		for(int i=1;i<=4;i++) {
			for(int j=0;j<4;j++) {
				if (i==a) cin>>v[1][j];
				else cin>>b;
			}
		}
		int s=0,t;
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				if (v[0][i]==v[1][j]) {
					s++;
					t=v[0][i];
					break;
				}	
			}
		}
		cout<<"Case #"<<k<<": ";
		if (s==1) {
			cout<<t<<endl;
		} else if (s>1) {
			cout<<"Bad magician!\n";
		} else {
			cout<<"Volunteer cheated!\n";
		}
	}
	return 0;
}