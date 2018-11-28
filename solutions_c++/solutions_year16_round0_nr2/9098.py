#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;

	scanf("%d", &t);

	string s;

	for(int cases = 1; cases <= t; cases++){
		int cont = 0;
		cin >> s;

		for(int i = 0; i < s.size() - 1; i++){
			if(s[i] != s[i + 1])
				cont++;
		}

		if(s[s.size() - 1] == '-')
			cont++;

    		printf("Case #%d: %d\n", cases, cont);
    		

	}

	return 0;
}
