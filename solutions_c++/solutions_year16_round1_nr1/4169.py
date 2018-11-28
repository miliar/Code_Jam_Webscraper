#include<iostream>
#include<cstdio>
#include<set>
#include<cstring>
#include<algorithm>
#include<list>

using namespace std;

void program(int t){
	char s[1005];

	scanf("%s",s);
	int len = strlen(s);
	list<char> ans;
	ans.push_back(s[0]);
	for(int i=1;i<len;i++){
		if(*ans.begin() <= s[i]){
			ans.push_front(s[i]);
		}
		else{
			ans.push_back(s[i]);	
		}	
	}
		
	printf("Case #%d: ",t);
	for(list<char>::iterator itr = ans.begin(); itr!=ans.end(); itr++){
		printf("%c",*itr);
	}
	printf("\n");
	
}
int main(){
	int t;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	int T = t;
	while(t--){
		program(T-t);
	}
	return 0;
}
