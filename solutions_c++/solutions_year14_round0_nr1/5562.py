#include <iostream>
using namespace std;

int main(){
	int t; cin >> t;
	for(int ca = 1; ca <= t; ca++){
		bool p[17];
		for(int i=0; i<17; i++) p[i] = true;
		
		int a;
		cin >> a; a--;
		for(int i=0; i<4; i++) for(int j=0; j<4; j++){
			int x; cin >> x;
			if(i != a) p[x] = false;
		}
		cin >> a; a--;
		for(int i=0; i<4; i++) for(int j=0; j<4; j++){
			int x; cin >> x;
			if(i != a) p[x] = false;
		}
		
		cout << "Case #" << ca << ": ";
		int x = 0;
		for(int i=1; i<=16; i++) if(p[i]) x++;
		if(x == 0) cout << "Volunteer cheated!";
		else if(x > 1) cout << "Bad magician!";
		else{
			for(int i=1; i<=16; i++) if(p[i]) cout << i;
		}
		cout << endl;
	}
	return 0;
}
