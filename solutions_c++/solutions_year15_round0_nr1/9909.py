#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main(){
	int cases;
	cin >> cases;
	for(int x=0; x<cases; ++x){
		int maxs=0,standed=0,need=0;
		string people="";
		cin >> maxs >> people;
		for(int i=0; i<people.size();++i){
			if(standed <i){
				if(people[i]=='0') continue;
				need += i-standed;
				standed += people[i] - '0' + need;
			}else{
				standed += people[i] - '0';
			}
		}
		printf("Case #%d: %d\n", x+1, need);
	}
}