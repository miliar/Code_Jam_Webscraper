#include <iostream>
int mushrooms[1000];
int d;
using namespace std;

int main () {
	int T;
	cin >>  T;
	int N;
	int y, z;
	
	for (int t=1; t<=T; t++) {
		
		cin >> N;
		y=0;
		z=0;
		int maxD=0;
		
		cin >> mushrooms[0];
		for (int i=1; i<N; i++) {
			cin >> mushrooms[i];
			if (mushrooms[i]<mushrooms[i-1])
				y = y + mushrooms[i-1]-mushrooms[i];
			
			if (mushrooms[i-1]-mushrooms[i]>maxD)
				maxD=mushrooms[i-1]-mushrooms[i];
		}
		
		for (int i=0; i<N-1; i++) {
			if (mushrooms[i]<maxD)
				z+=mushrooms[i];
			else
				z+=maxD;
		}
		
		cout << "Case #" << t << ": " << y << ' ' << z << endl;
	}
	
	return 0;
}
