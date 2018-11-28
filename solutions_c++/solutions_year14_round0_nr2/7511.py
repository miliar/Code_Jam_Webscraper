#include <iostream>
#include <iomanip>

using namespace std;

void process_case(int case_id)
{
	double C, F, X;
	cin >> C >> F >> X;

	double t = 0.0;
	double p = 2.0;
	double a = X / p;
	double b = C / p + X / (p + F);
	while(a > b) {
		t = t + C / p;
		p = p + F;
		a = X / p;
		b = C / p + X / (p + F);
	}
	t = t + X / p;
	cout << "Case #" << case_id << ": ";
	cout << setiosflags(ios::fixed) << setprecision(7) << t << endl;
}

int main()
{
	int T;
	cin >> T;
	
	int i = 1;
	while(i <= T) {
		process_case(i);
	
		++ i;
	}
	
	return 0;
}