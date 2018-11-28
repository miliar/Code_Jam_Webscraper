#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
char str[1005];
char res[2005];
int main()
{
	//freopen("xx.in" , "r" , stdin);
	//freopen("yy.out" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	for(int ca = 1 ; ca <= t ; ca++) {
		scanf("%s" , str);
		printf("Case #%d: " , ca);
		int len = strlen(str);
		if(len == 1) {
			printf("%c\n" , str[0]);
			continue;
		}
		char Max = str[0];
		int l = 1000 , r = 1000;
		res[l] = Max;
		for(int i = 1 ; i < len ; i++) {
			if(str[i] >= Max) {
				res[--l] = str[i];
				Max = str[i];
			}
			else {
				res[++r] = str[i];
			}
		}
		for(int i = l ; i < r ; i++) {
			printf("%c" , res[i]);
		}
		printf("%c\n" , res[r]);
	}
}