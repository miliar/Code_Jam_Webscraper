// Submitted by Silithus @ Macau
#include <iostream>
#include <iomanip>

using namespace std;

double work(void)
{
	double C,F,X,prod=2.0,ans=0.0,t1,t2;
	
	cin >> C >> F >> X;

	do {
		t1 = X / prod;
		t2 = C/prod + X/(prod+F);
		if( t2 < t1 ) {
			ans += C / prod;
			prod += F;
		} else {
			ans += t1;
			break;
		}
	} while( 1 );

	return ans;
}

int main(void)
{
	int t,T;

	cin >> T;
	for(t=1; t<=T; t++)
		cout << "Case #" << t << ": " << fixed << setprecision(7) << work() << endl;
	
	return 0;
}
