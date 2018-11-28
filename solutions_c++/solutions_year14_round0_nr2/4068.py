
// C - quantidade para comprar uma fazenda 
// F - quantidade ganaha por segundo com uma fazenda
// X - quantidade objetivo


// incialmente (sem fazenda) Ans = X / 2
// com uma fazenda
// 	- tempo para comprar a fazenda = C / 2
// 	- tempo para o objetivo = X / 6
// 	Ans = X / 6 + C / 2

// com duas fazendas
// 	- tempo para a segunda fazenda = C / 6
// 	- tempo para o objetivo = X / 10
// 	Ans = X / 10 + C / 2 + C / 6

// time  = X / (2 + farms * F) + C / 2 + C / (2 + F) + C / (2 + 2 * F) + C / (2 + )
// Ideia - aumentar quantidade de fazendas enquanto da lucro de tempo

#include <iostream>
#include <iomanip>

void test();

using namespace std;

int main() {
	int T;
	cout << fixed << setprecision(8);

	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		test();
	}
}

void test() {
	double c, f, x;
	cin >> c >> f >> x;

	double ans = x / 2.0;
	double farm_time = 0.0;
	int farms = 0;

	while(true) {
		//Create a farm
		farm_time += c / (2.0 + farms * f);
		farms++;

		double t = x / (2.0 + farms * f) + farm_time;
		
		if(t < ans) {
			ans = t;
		} else {
			break;
		}
		// cout << farms << " " << ans << endl;
	}

	cout << ans << '\n';
}