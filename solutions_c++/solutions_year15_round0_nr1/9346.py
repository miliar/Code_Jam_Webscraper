//============================================================================
// Name        : A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>

using namespace std;

int main() {

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);


	int t;
	cin >> t;
	for (int j = 0; j < t; j++){
		int s;
		cin >> s;
		string kol;
		getline(cin, kol);
		kol.erase(0,1);
		int ans = 0;
		int people = (char) kol[0] - 48;
		//cout << kol[0] <<" people=" << people << endl;
		for (int i = 1; i < s +1; i++){
			//cout << i <<" people " << people << endl;
			if (people < i){
				ans += i - people;
				people = i;
			}
			people += (char) kol[i] - 48;
		}
		cout << "Case #" << j + 1 << ": " << ans << endl;
	}

	fclose(stdin);
	fclose(stdout);


	return 0;
}
