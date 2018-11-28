#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int t, tCounter, N;
	cin >> t;
	int i;
	string s;
	int len, ref, flips;
	bool pan[100];
	for (tCounter = 1; tCounter <= t; tCounter++) {
		cin >> s;
		len=s.length();
		for (i = 0; i < len; i++)
			pan[i]=(s[i]=='+');
		ref=pan[0];
		flips=0;
		for (i = 0; i<len; i++) {
			if (pan[i]!=ref) {
				flips++;
				ref=!ref;
			}
		}
		if (!pan[len-1])
			flips++;
		
		cout << "Case #" << tCounter << ": ";
		cout << flips ;
		cout << endl;
	}
	return 0;
}

