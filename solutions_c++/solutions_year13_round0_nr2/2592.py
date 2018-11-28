#include <iostream>

using namespace std;

int T;
int a,b;
bool f1,f2;
int t[200][200];

int main() {
	cin >> T;
	for(int x=1;x<=T;x++) {

		bool ans = true;
		cin >> a >> b;
		for(int i=1;i<=a;i++)
			for(int j=1;j<=b;j++) cin >> t[i][j];

		for(int i=1;i<=a;i++) {
			for(int j=1;j<=b;j++) {
				f1 = f2 = false;
				int m = 0;
				for(int z = 1;z<=b;z++) m = max(m,t[i][z]);
				if(m > t[i][j]) f1 = true ;
				m = 0;
				for(int z = 1;z<=a;z++) m = max(m,t[z][j]);
				if(m > t[i][j]) f2 = true;


				if(f1 && f2) ans = false;
			}
		}
		if(ans) cout << "Case #"<<x <<": YES"<< endl; else
		cout << "Case #"<<x <<": NO"<< endl;
	}
	return 0;
}
