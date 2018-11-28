#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

const char number[10][10]={
"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

bool flag;

int a[10][26],b[26],c[10],lim[10];

bool check(int k){
	int sum[26];
	memset(sum,0,sizeof(sum));
	for (int i=0;i<=k;i++){
		for (int j=0;j<strlen(number[i]);j++){
			sum[number[i][j]-'A']+=c[i];
			if (sum[number[i][j]-'A']>b[number[i][j]-'A']) return 0;
		}
	}
	return 1;
}

bool fit(){
	int sum[26];
	memset(sum,0,sizeof(sum));
	for (int i=0;i<=9;i++){
		for (int j=0;j<strlen(number[i]);j++){
			sum[number[i][j]-'A']+=c[i];
			if (sum[number[i][j]-'A']>b[number[i][j]-'A']) return 0;
		}
	}
	for (int i=0;i<26;i++)
		if (b[i]!=sum[i]) return 0;
	return 1;
}

void dfs(int d){
	int i;
	if (d>9){
		if (fit()) flag=1;
		return;
	}
	for (i=lim[d];i>=0;i--){
		c[d]=i;
		if (check(d))
			dfs(d+1);
		if (flag) return;
	}
}

int main(){
	for (int i=0;i<10;i++){
		for (int j=0;j<strlen(number[i]);j++)
			a[i][number[i][j]-'A']++;
	}

	int tt;
	char s[2005];
	cin>>tt;
	for (int cs=1;cs<=tt;cs++){
		printf("Case #%d: ",cs);
		scanf("%s",s);
		flag=0;
		memset(b,0,sizeof(b));
		int l=strlen(s);
		for (int i=0;i<l;i++){
			b[s[i]-'A']++;
		}
		for (int i=0;i<10;i++){
			lim[i]=-1;
			for (int j=0;j<strlen(number[i]);j++){
				int x=b[number[i][j]-'A']/a[i][number[i][j]-'A'];
				if (lim[i]==-1 || x<lim[i])
					lim[i]=x;
			}
		}
		dfs(0);
		for (int i=0;i<10;i++)
			for (int j=1;j<=c[i];j++)
				printf("%d",i);
		printf("\n");
	}

	return 0;
}