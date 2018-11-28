#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;	
	
	scanf("%d", &t);

	for(int cases = 1; cases <= t; cases++){
		int n;
		string s;

		scanf("%d", &n);

		cin >> s;

		int cont = s[0] - '0';
		int invited = 0;

		for(int i = 1; i < s.size(); i++){
			if(cont < i){
				invited += i - cont;
				cont = i;
			}

			cont += s[i] - '0';
		}

		printf("Case #%d: %d\n", cases, invited);
	}

	return 0;
}
