#include <iostream>
using namespace std;

#define N 6

int checkmino(int x, int r, int c){
	if(x==4 && (r<=2 || c <= 2)) return -1;

	for(int i=0;i<=x/2;i++){
		int minox = i+1, minoy = x-i;
		//cout << minox << " " << minoy << endl;
		if((r<minox || c<minox) && (r<minoy || c<minoy)) return -1;
	}
	return 0;
}	

int calc(int now){
	int x, r, c;
	cin >> x >> r >> c;

	if((r*c)%x > 0 || checkmino(x,r,c) == -1)
		cout << "Case #" << now << ": RICHARD" << endl;
	else
		cout << "Case #" << now << ": GABRIEL" << endl;

	return 0;
}

int main() {
	int n; cin >> n;

	for(int i=0;i<n;i++)
		calc(i+1);

	return 0;
}