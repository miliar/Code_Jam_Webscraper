#include <bits/stdc++.h>

using namespace std;

int main(){
	int i,j,k;
	int t;
	char s[2000];
	int count = 0;
	cin >> t;
	fgets(s, 2, stdin);
	for (i = 0; i < t; i++){
		fgets(s, 200, stdin);
		j = 0;
		for(k = 0; s[j] != '\n'; k++){
			int change = s[0]=='-'?'+':'-';
			for(j = 0; s[j] != '\n' && s[j] != change; j++){
				s[j] = change;
			}
			if (s[j] != '\n' || s[0] == '+')
				count++;
		}
		cout << "Case #" << i+1 << ": ";
		cout << count << endl;
		count = 0;
	} 
	return 0;
}