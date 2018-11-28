#include <stdio.h>
#include <string.h>

#include <deque>

using namespace std;

int main(void){

	int testcase;
	scanf("%d", &testcase);

	for(int t_itr = 1; t_itr <= testcase; t_itr++){

		char str[1111];
		scanf("%s", str);

		int len = strlen(str);

		deque<char> dq;
		dq.push_back(str[0]);
		for(int i=1; i<len; i++){
			if(dq.front() <= str[i]){
				dq.push_front(str[i]);
			}
			else{
				dq.push_back(str[i]);
			}
		}

		printf("Case #%d: ", t_itr);
		for(auto itr = dq.begin(); itr != dq.end(); itr++){
			printf("%c", *itr);
		}
		printf("\n");

		
	}
}