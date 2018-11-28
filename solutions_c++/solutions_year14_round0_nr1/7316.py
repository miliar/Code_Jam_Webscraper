#include <iostream>
#include <fstream>
using namespace std;
int main(){
	int T, a[16], b[16], c[16], aa, bb, ans;
	ofstream SaveFile("a.txt");
	cin>>T;
	for (int n = 0; n < T; ++n){
		cin>>aa;
		for (int i = 0; i < 16; ++i) cin>>a[i];
		cin>>bb;
		for (int i = 0; i < 16; ++i) cin>>b[i];
		for (int i = 0; i < 16; ++i) c[i] = 0;
		for (int i = 0; i < 4; ++i){
			c[a[(aa-1)*4+i]-1]++;
			c[b[(bb-1)*4+i]-1]++;
		}
		ans = -1;
		for (int i = 0; i < 16; ++i){
			if (c[i] == 2){
				switch (ans){
					case -1:
						ans = i+1;
						break;
					case -2:
						break;
					default:
						ans = -2;
				}
			}
		}
		SaveFile<<"Case #"<<n+1<<": ";
		switch (ans){
			case -1:
				SaveFile<<"Volunteer cheated!"<<endl;
				break;
			case -2:
				SaveFile<<"Bad magician!"<<endl;
				break;
			default:
				SaveFile<<ans<<endl;
		}
	}
	return 0;
}