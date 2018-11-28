// test1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

int findFriendNum(int smax, char* s)
{
	int current_num = 0;
	int friend_req = 0;

	for (int i = 0; i < smax + 1; i++){
		if (current_num + (int)(s[i] - '0') < i + 1){
			friend_req++;
			current_num++;
		}
		current_num += (s[i] - '0');
	}
	return friend_req;
}
int _tmain(int argc, _TCHAR* argv[])
{
	int T, i;
	scanf_s("%d", &T);
	for (i = 0; i < T; i++){
		int smax;
		char s[1001];
		scanf_s("%d %s", &smax, &s, 1001);
		printf("Case #%d: %d\n", i+1, findFriendNum(smax, s));
	}
	return 0;
}

