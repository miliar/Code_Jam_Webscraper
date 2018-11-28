#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>
using namespace std;
bool ok(char* s,int len){
	for(int i = 0; i < len; i++){
		if(s[i] == '-')return false;
	}
	return true;
}
int ans;
int rev_from_end(char* s,int len){
	for(int i = len-1; i >= 0; i--){
		if(s[i] == '-'){
			return i;
		}
	}
	return -1;
}
void rev_from_start(char* s,int len){
	int tmp,tmp2;
	for(int i = 0; i < len; i++){
		if(s[i] == '-'){
			tmp = i;
			break;
		}
	}
	int l = 0,r = tmp-1;
	for(int i = l; i <= r; i++)s[i] = '-';
	if(r>=l)ans++;
	tmp2=len-1;
	for(int i = tmp; i < len; i++){
		if(s[i] == '+'){
			tmp2 = i-1;
			break;
		}
	}
	l = 0,r = tmp2;
	if(tmp2>=0)ans++;
	while(l<r){
		swap(s[l],s[r]);
		l++,r--;
	}
	for(int i = 0; i <= tmp2; i++){
		if(s[i] == '+')s[i] = '-';
		else s[i] = '+';
	}
}
char s[200];
int length;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	//printf("T = %d\n",T);
	for(int i = 1; i <= T; i++){
		scanf(" %s",s);
	//	printf("I = %d ,S = %s\n",i,s);
		length = strlen(s);
		ans=0;
		while(1){
			if(ok(s,length))break;
			length = rev_from_end(s,length)+1;
			//printf("len = %d\n",length);
			//printf("S1 = %s:\n",s);
			if(ok(s,length))break;
			rev_from_start(s,length);
			//printf("S2 = %s:\n",s);
			//ans+=2;
			//getchar();
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
} 
