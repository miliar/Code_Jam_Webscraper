#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int num[26];
char s[2005];
string ID[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
bool DFS(int now,int n,string ans){
	int f[26],m;
	if (n==0){
		puts(ans.c_str());
		return true;
	}
	while (now<10){
		bool flag=true;
		m=ID[now].length();
		for (int i=0;i<26;i++)
			f[i]=num[i];
		for (int i=0;i<m;i++){
			int x=ID[now][i]-'A';
			if (num[x]!=0){
				num[x]--;  
			}else{
				flag=false;
				break;
			}
		}
		if (flag && DFS(now,n-m,ans+(char)(now+'0'))) return true;
		for (int i=0;i<26;i++)
			num[i]=f[i];
		now++;
	}
	return false;
}
int main(){
	int T;
	freopen("A-small-attempt0.in.txt","r",stdin);
	freopen("A-small-attempt0.in.out","w",stdout); 
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++){
		scanf("%s",s);
		printf("Case #%d: ",cases);
		int n=strlen(s);
		memset(num,0,sizeof(num));
		for (int i=0;i<n;i++)
			num[s[i]-'A']++;
		DFS(0,n,"");
	}
	return 0;
}