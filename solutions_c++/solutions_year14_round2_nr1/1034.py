#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>


#define MAX 110

using namespace std;

char s[MAX][MAX];

int n;
int cnt[MAX][MAX];
bool fail ;
int cost(int col){
	int num[MAX],m=0;
	int mid;
	int sum = 0;
	for(int i = 0;i<n;++i)
	num[m++]=cnt[i][col];
	sort(num,num+m);
	mid = num[m/2];
	for(int i = 0;i<m;++i)
	sum+=abs(num[i]-mid);
	return sum;
}
int solve(){
	int index = 0;
	int sum = 0;
	for(int i = 0; i < n; ++i){
		index = 1;
		cnt[i][0]=1;
		for(int j = 1; s[i][j]!='\0';++j){
			if(s[i][j]!=s[i][j-1]){
				s[i][index++]=s[i][j];
				cnt[i][index-1]=1;
			}
			else{
				cnt[i][index-1]++;
			}
		}
		s[i][index]='\0';
	}
	fail = false;
	for(int i = 1; i < n; ++i){
		if(strcmp(s[i],s[i-1]))
		fail = true;
	}
	for(int i = 0;s[0][i]!='\0';++i)
	sum+=cost(i);
	return sum;
}

int main(){
	int t,i;
	int result;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		scanf("%d",&n);
		for(int i = 0; i < n; ++i){
			scanf("%s",s+i);
		}
		result = solve();
		if(fail)
		printf("Case #%d: Fegla Won\n",i);
		else
		printf("Case #%d: %d\n",i,result);
	}
	return 0;
}
