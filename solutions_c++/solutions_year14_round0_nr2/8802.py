#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

// ifstream fin("test.in"); // 
// ofstream fout("test.out"); // 

int T;
double C, vF, X;
long double opt[2], pr;
long double speed;

void solve(){
	int i = 0, p = 10;
	cin >> C >> vF >> X; // 

	speed = 2;
	opt[i++] = X / 2;
	speed += vF;
	opt[i] = C / 2 + X / speed;

	while (opt[i % 2] < opt[(i - 1) % 2]){
		i++;

		opt[i % 2] = opt[(i - 1) % 2] - X / speed;
		opt[i % 2] += C / speed;

 		speed += vF;
		opt[i % 2] += X / speed;
	}

	cout << int(opt[(i - 1) % 2]) << '.'; // 
	pr = opt[(i - 1) % 2] - int(opt[(i - 1) % 2]);
	for (i = 0; i < 8; i++){
		pr *= 10;
		cout << int(pr); // 
		pr -= int(pr);
	}

}

int main(){
	int i;
	cin >> T; // 
	
	for (i = 1; i <= T; i++){
		cout << "Case #" << i << ": "; // 
			solve();
		cout << '\n'; // 
	}
	
	return 0;
}