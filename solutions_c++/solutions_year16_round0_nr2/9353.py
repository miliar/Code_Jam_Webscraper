#include <cstdio>

int t;
char s[105], temp[105];

int flip(){
	int i = 1, j = 0, count = 0;
	char last = s[0];
	while(s[i]!='\0'){
		if(last=='-'){
			if(s[i]=='+'){
				count++;
			}
		}
		else{
			if(s[i]=='-'){
				count++;
			}
		}
		last = s[i];
		i++;
	}
	if(last=='-'){
		count++;
	}
	return count;
}



main(){
	scanf("%d", &t); //testcase
	for(int i=1; i<=t; i++){
		scanf("%s", &s);
		printf("Case #%d: %d\n", i,flip());

	}

}