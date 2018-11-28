/*************************************************************************
    > File Name: b.cpp
    > Author: james47
    > Mail: 
    > Created Time: Sat Apr  9 16:32:54 2016
 ************************************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

int T, cas;
char s[110];

int work(){
	int len = strlen(s);
	int ret = 0;
	for (int i = 0; i < len; i++)
		if (s[i] == '-'){
			if (i == 0) ret ++;
			else if (s[i-1] != '-') ret += 2;
		}
	return ret;
}

int main()
{
	scanf("%d", &T);
	while(T--){
		scanf("%s", s);
		printf("Case #%d: %d\n", ++cas, work());
	}
	return 0;
}
