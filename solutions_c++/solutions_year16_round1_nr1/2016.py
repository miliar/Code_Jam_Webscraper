#include <bits/stdc++.h>
using namespace std;
int n;
char S[1010];
deque<char> D;
int main(){
	int t;
	scanf("%d", &t);
	for(int c=1; c<=t; c++){
		scanf("%s", S);
		n = strlen(S);
		D.push_front(S[0]);
		for(int i=1; i<n; i++){
			if(S[i] >= D[0]) D.push_front(S[i]);
			else D.push_back(S[i]);
		}
		printf("Case #%d: ", c);
		for(int i=0; i<n; i++) printf("%c", D[i]);
		printf("\n");
		D.clear();
	}
	return 0;
}