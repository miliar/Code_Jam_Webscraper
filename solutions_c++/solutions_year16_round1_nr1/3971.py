#include <bits/stdc++.h>

using namespace std;

int main(){
	int cases;
	scanf("%d", &cases);

	for(int e = 0; e<cases; e++){
		string str;
		cin >> str;

		deque<char> dq;

		for(int i = 0; str[i]; i++){
			if(dq.empty()){
				dq.push_back(str[i]);
			} else {

				if(str[i] >= dq.front()){
					dq.push_front(str[i]);
				} else {
					dq.push_back(str[i]);
				}

			}
		}

		printf("Case #%d: ", e+1);
		while(!dq.empty()){
			printf("%c", dq.front());
			dq.pop_front();
		}
		printf("\n");

	}	

	return 0;
}