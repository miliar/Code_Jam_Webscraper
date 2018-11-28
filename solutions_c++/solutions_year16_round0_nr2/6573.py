#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main() {
	int T,i,cpt;
	string stack;
	cin >> T;
	for(i = 1 ; i <= T ; i++){
		cin >> stack;
		cpt=0;
		for(int j = 0 ; j < stack.length()-1 ; j++)
			if(stack[j]!=stack[j+1])
				cpt++;
		if(stack[stack.length()-1]=='-')
			cpt++;
		printf("Case #%d: %d\n",i,cpt);
	}
	return 0;
}
