#include <iostream>
using namespace std;

int main() {
	int cases;
	cin>>cases;

	int c=1;
	while(cases--) {
		int S[1005];

		int t=0;
		
		int s;

		string ppl;
		cin >> s >> ppl;

		for(int i=0; i<=s; i++)
			S[i] = ppl[i]-'0';

		int sum=S[0];

		for(int i=1; i<=s; i++) {
			if(i>sum) {
				int a=i-sum;
				t+=a;
				sum+=a;
			}
			sum += S[i];
		}

			cout << "Case #" << c++ << ": " <<  t << endl;


	}


	return 0;
}