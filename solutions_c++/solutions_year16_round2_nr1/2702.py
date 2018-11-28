#include <cstdio>
#include <cstring>

void run(int r) {
	char str[3000] = {};
	char num[10][10] = {"ZERO", "EIGHT" ,"TWO", "SIX", "SEVEN", "FIVE" , "FOUR", "ONE", "THREE", "NINE"};
	int p[10] = {0,8,2,6,7,5,4,1,3,9};
	int q[10] = {};
	int x[10] = {'Z'-'A','G'-'A','W'-'A','X'-'A','S'-'A','V'-'A','F'-'A','O'-'A','R'-'A','I'-'A'};
	int n[10] = {};
	int count[26] = {};
	scanf("%s",str);
	for(int i=0;str[i]!='\0';i++)
		count[str[i]-'A']++;
	printf("Case #%d: ",r);
	for(int i=0;i<10;i++) {
		int len = strlen(num[i]);
		//printf("%d",count[x[i]]);
		q[p[i]] += count[x[i]];
		int tmp = count[x[i]];
		for(int j=0;j<len;j++)
			count[num[i][j]-'A'] -= tmp;
	}
	for(int i=0;i<10;i++)
		for(int j=0;j<q[i];j++)
			printf("%d",i);
	printf("\n");
}

int main() {
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
		run(i);
}