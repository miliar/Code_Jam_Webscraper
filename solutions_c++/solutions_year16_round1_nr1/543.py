#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int t, tCounter, N;
	cin >> t;
	int i;
	string in, out;
	for (tCounter = 1; tCounter <= t; tCounter++) {
		cout << "Case #" << tCounter << ": ";
		cin >> in;
		out = in[0];
		for (i=1;i<in.length();i++) {
			if (in[i]>=out[0])
				out=in[i]+out;
			else
				out=out+in[i];
		}
		cout <<  out;
		cout << endl;
	}
	return 0;
}

