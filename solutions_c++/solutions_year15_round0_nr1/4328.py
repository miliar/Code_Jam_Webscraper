#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int i=1;i <=T; i++) {
		int Smax,sum=0,total=0;
		string Ser;		
		cin >> Smax >> Ser;
		for(int j=0; j <= Smax; j++) {
			int k = Ser[j] - 48;
			if(total >= j)
				total+=k;
			else {
				int l = (j-total);
				total+=(l+k);
				sum+=l;
			}
		}
		cout << "Case #"<< i << ": " << sum << endl;
	}
	return 0;
}
