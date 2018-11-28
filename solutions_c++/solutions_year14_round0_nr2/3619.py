
#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;


int main(int argc, char** argv){

	int T, n;
	double C, F, X;
	double B, t, intt;
	double buyTime, dBuyTime; 
	
	cin >> T;

	for( int i=1; i <= T; i++ ){
		cin >> fixed >> setprecision(7) >> C >> F >> X;
		//cout << fixed << setprecision(7) << C << " " << F << " " << X << endl;

		B = 0.0;
		t = 0.0;
		n = 0;

		while( B < X ){
			intt = min(C, X-B) / (2 + n*F);

			t += intt;
			B += 2*intt + n*F*intt;

			buyTime = (X - (B-C)) / (2 + (n+1)*F);
			dBuyTime = (X-B) / (2 + n*F);

			if( buyTime < dBuyTime ){
				//BUY
				n++;
				B -= C;
			}
			//else{
				//DO NOT BUY
			//}

		}

		cout << fixed << setprecision(7) << "Case #" << i << ": " << t << endl;

	}

	return 0;
}











