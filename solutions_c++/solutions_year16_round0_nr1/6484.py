#include <iostream>

using namespace std;

int main () {
	int T,N,count,number;
	cin >> T;
	bool seen[10];
	for(int i=1;i<=T;i++) {
		cin >> N;
		cout << "Case #" << i <<": ";
		if(N==0)
			cout << "INSOMNIA" << endl;
		else {
			for(int j = 0 ; j < 10 ; j++)
				seen[j]=false;
		  count=1;
			number=N;
			while(!seen[0] || !seen[1] || !seen[2] || !seen[3] || !seen[4] ||
				 	!seen[5] || !seen[6] || !seen[7] || !seen[8] || !seen[9]) {
				if(number!=0) {
					seen[number%10]=true;
				  number/=10;
				}
				else {
					count++;
					number=N*count;
				}
			}
			cout << N*count << endl;
		}
			
	}
	return 0;
}
