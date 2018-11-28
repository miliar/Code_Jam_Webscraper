//============================================================================
// Name        : CodeJam.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Problem A. Standing Ovation
//============================================================================

#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int needFriend(char p[],int s){
	int numFriend=0,newFriend=0;
	for(int i=0;i<s;i++){
		if(numFriend < i){
			newFriend+=i-numFriend;
			numFriend+=i-numFriend+(p[i]-'0');
		}else if(p[i]-'0'>0){
			numFriend+=p[i]-'0';
		}
	}
	return newFriend;
}

int main() {
	int T,S;
	char people[1002];
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%d %s",&S,people);
		printf("Case #%d: %d\n",i+1,needFriend(people,S+1));
	}
	return 0;
}
