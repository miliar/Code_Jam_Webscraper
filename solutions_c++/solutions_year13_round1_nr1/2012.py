// Bullseye.cpp -MysticBoy

#include <iostream>
#include <string>
//#include <cstdlib>
//#include <cstdio>

using namespace std;

int main(int cmdcount, char **cmdlist)
{
	int T; 			//number of test cases, T: 1 ≤ T ≤ 1000. 
	int long long r, t;		//1 ≤ r, t ≤ 1000. 
	int long i, j, k, l, m;



	// input
	cin >> T;
	int result[T+1];
	char blank;

	for(k = 1; k <= T; ++k) {
		cin >> r >> t;
		int long long count = 0;
		int long long inner = r;
		int long long outer = inner + 1;
		int long long area = 0;
		//cout << r << "	" << t << endl;
		while(1) {
			area = outer * outer - inner * inner;
			//cout <<"area: " << area << endl;
			if( area <= t ) {
				count++;
				inner +=2;
				outer +=2;	
				t = t - area;
			}
			else {
				cout <<"Case #"<< k <<": "<< count << endl;
				break;
			}			
		}
	}

	// processing

	//cout << "-------------------------" << endl;
	/*for(k = 1; k <= T; ++k) 
		cout <<"Case #"<< k <<": "<< result[k] << endl;
	/* */
	return 0;
}	//End main


