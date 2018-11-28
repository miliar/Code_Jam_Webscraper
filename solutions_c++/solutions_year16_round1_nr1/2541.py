#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int test;
	scanf("%d",&test);
	for(int tc = 1; tc <= test; tc++) {
		char word[1005];
		deque<char> dq;
		scanf("%s",word);
		int leng = strlen(word);
		for(int i = 0; i < leng; i++) {
			if(i == 0) {
				dq.push_front(word[i]);
			}
			else {
				if(dq.front()>word[i]) {
					dq.push_back(word[i]);
				}
				else dq.push_front(word[i]);
			}
			
		}
		printf("Case #%d: ",tc);
		while(!dq.empty()) {
			printf("%c",dq.front());
			dq.pop_front();
		}
		printf("\n");
	}
	return 0;
}
