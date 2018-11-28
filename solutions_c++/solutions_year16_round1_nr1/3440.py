#include<stdio.h>
#include<string.h>
#include<deque>

using namespace std;

int T;
char str[101][1005];
deque<char> ans;
deque<char>::iterator it;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k;
	char flag;
	scanf("%d",&T);
	for(k=1;k<=T;k++){
		scanf("%s",&str[k]);
		for(i=0;i<strlen(str[k]);i++){
			if(ans.front()<=str[k][i])ans.push_front(str[k][i]);
			else ans.push_back(str[k][i]);
		}
		printf("Case #%d: ",k);
		for(it = ans.begin();it != ans.end(); it++)printf("%c",*it);
		for(i=0;i<strlen(str[k]);i++)ans.pop_front();
		printf("\n");
	}
	
	return 0;
}
