#include <deque>
#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

deque<char> s;
string slovo;
int t;

int main(void){
	scanf("%d", &t);
	for(int test =1; test <=t;test++){
		cin >> slovo;
		printf("Case #%d: ", test);
		s.push_back(slovo[0]);
		for(int i = 1; i < slovo.length(); i++){
			if(s.front()>slovo[i])
				s.push_back(slovo[i]);
			else
				s.push_front(slovo[i]);
		}
		while(s.size()){
			cout << s.front();
			s.pop_front();
		}
		printf("\n");
	}
	return 0;
}
