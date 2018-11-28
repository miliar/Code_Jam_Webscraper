#include <iostream>
#include <iomanip>

using namespace std;

int main()
{

	cout << setprecision(7); 
	cout << setiosflags(ios::fixed); 
	int T;
	cin >> T;

	for(int i=1;i<=T;i++){
		double C, F, X;

		cin >> C;
		cin >> F;
		cin >> X;

		double t_prev = 0.0;
		double a_prev = 2.0;
		double b_prev = 0.0;
		double time_prev = (X - b_prev) / a_prev;
		while(1){
			double t = t_prev + C / a_prev;
			double a = a_prev + F;
			double b = -1.0 * a * t;
			double time = (X - b) / a;

			if (time_prev < time) {
				break;
			}

			t_prev = t;
			a_prev = a;
			b_prev = b;
			time_prev = time;
		}
		cout << "Case #" << i << ": ";
		cout << time_prev;
		cout << endl;
		
	}
}
