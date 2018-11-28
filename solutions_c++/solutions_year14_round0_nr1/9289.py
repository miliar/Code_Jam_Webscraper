#include <iostream>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int i=0; i<T; ++i){
		int a;
		int b[4];
		cin >> a;
		for(int j=0; j<4; ++j){
			for(int k=0; k<4; ++k){
				int tmp;
				cin >> tmp;
				if(j+1==a) b[k]=tmp;
			}
		}
		int count=0;
		int ans;
		cin >> a;
		for(int j=0; j<4; ++j){
			for(int k=0; k<4; ++k){
				int tmp;
				cin >> tmp;
				if(j+1==a&&count<2){
					for(int l=0; l<4; ++l){
						if(tmp==b[l]){
							ans=b[l];
							++count;
							break;
						}
					}
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		if(count==0) cout << "Volunteer cheated!\n";
		else if(count==1) cout << ans << endl;
		else cout << "Bad magician!\n";
	}
	return 0;
}
