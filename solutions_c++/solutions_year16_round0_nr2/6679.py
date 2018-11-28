#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;
void program(int t){
	char s[105];
	scanf("%s",s);
	int len = strlen(s);
	int seg = 1;
	for(int i=1; i<len; ++i){
		if(s[i] != s[i-1]){
			seg++;
		}
	}
	//printf("seg = %d\n",seg);
	int ans = 0;
	if(s[len-1] == '+'){
		ans = seg-1;
	}else{
		ans = seg;
	}
	
	printf("Case #%d: %d\n",t,ans);
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
}
