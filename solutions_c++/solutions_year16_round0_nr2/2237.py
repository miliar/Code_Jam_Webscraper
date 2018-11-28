
#include <cstdio>
#include <algorithm>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

int getMin(char *s){
	char tmp = s[0];
	int count = 0;
	int i;
	for (i = 0; i < strlen(s) ; i++){
		if(tmp != s[i]){
			count++;
			tmp = s[i];
		}
	}
	if(s[i-1] =='-'){
		count++;
	}
	
	return count;
}

int main()
{	
	//inputFile = fopen("A-small-attempt0.in", "r");
	//inputFile = fopen("input.txt", "r");
	//outputFile = fopen("output.txt", "w");
	freopen("B-small-attempt0.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tCase;
	int n;
	char s[100];
	int result = 0;
	scanf("%d", &tCase);
	gets(s);
	
	for (int i = 1 ; i <= tCase ; i++){
		gets(s);
		//puts(s);
		printf("Case #%d: %d\n",i, getMin(s));
	} 
	
	return 0;
}


