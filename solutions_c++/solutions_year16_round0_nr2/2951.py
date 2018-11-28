#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <string>


using namespace std;


int main(){
	bool men;

	string s;
	int casos;
	int sol;
	cin >> casos;

	for (int i = 1; i <= casos; i++){
		sol = 0;
		cin >> s;
		men = 1;
		for (int k = s.size() - 1; k >= 0; k--){
			if (men and s[k] =='-'){
				men = 0;
				sol++;
			}
			if (!men and s[k] == '+'){
				men = 1;
				sol++;
			}
		}

		printf("Case #%d: %d\n",i,sol);

	}



}