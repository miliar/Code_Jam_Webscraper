#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int t, tCounter, N;
	cin >> t;
	long long int i, counter, s;
	bool digit[10], check, myContinue;
	for (tCounter = 1; tCounter <= t; tCounter++) {
		cin >> N;
		if (N==0)
			check=true;
		else
			check=false;
		counter=0;
		for (i = 0; i < 10; i++)
			digit[i]=false;

		while(!check) {
			s = (counter + 1) * N;
			while(s) {
				digit[(s % 10)] = true;
				s = s / 10;
			}

			check=true;
			for (i = 0; i < 10; i++)
				if (digit[i]==false)
					check=false;
			counter++;
		}
		
		cout << "Case #" << tCounter << ": ";
		if (counter==0)
			cout << "INSOMNIA" ;
		else
			cout << counter * N;
		cout << endl;
	}
	return 0;
}

