#include <algorithm>
#include <iostream>

using namespace std;

bool cmp(int a, int b){ return a > b; }

int r;
void btk(int arr[51], int c){
	int tMax = arr[0];
	if (tMax < 4) return;
	
	int cpy[51];
	for (int i = 0; i < 51; i++) cpy[i] = arr[i];
	
	if (tMax == 9){
		int cpy2[51];
		for (int i = 0; i < 51; i++) cpy2[i] = arr[i];

		cpy2[0] = 6; cpy2[50] = 3;
		sort(cpy2, cpy2 + 51, cmp);
 		if (r > cpy2[0] + c) r = cpy2[0] + c;
		btk(cpy2, c + 1);
	}
	cpy[50] = (cpy[0] / 2) + cpy[0] % 2;
	cpy[0] = cpy[0] / 2;
	sort(cpy, cpy + 51, cmp);
	if (r > cpy[0] + c) r = cpy[0] + c;
	btk(cpy, c + 1);
}

void logic(){
	int origin[51] = { 0 };
	int d, c = 0;
	cin >> d;
	for (int i = 0; i < d; i++){
		cin >> origin[i];
		if (c < origin[i]) c = origin[i];
	}
	r = c;
	sort(origin, origin + 51, cmp);
	btk(origin, 1);

	cout << r << endl;
}
int main(){

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++){
		cout << "Case #" << i << ": ";
		logic();
	}
}