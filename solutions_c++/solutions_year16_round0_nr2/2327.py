#include <iostream>
#include <string>
using namespace std;

int main() {
	int x;
	cin >> x;
	
	for(int i=0;i<x;i++){
		string y; int ylen, ans=0;
		cin >> y;
		ylen = y.length();

		char prev=y[0];
		for(int l=1;l<ylen;l++){
			if(y[l] != prev){
				ans++;
				prev = y[l];
			}
		}

		if(y[ylen-1] == '-') ans++;
		
		cout << "Case #" << i+1 << ": " << ans << endl;
	}

	return 0;
}