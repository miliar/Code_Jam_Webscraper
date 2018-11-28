#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstring>
using namespace std;
string mp[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"},str;
bool contain(string &str,string tmp)
{
	for(int i=0;i<tmp.length();i++){
		if(str.find(tmp[i])==-1){
			return 0;
		}
	}
	for(int i=0;i<tmp.length();i++){
		int t=str.find(tmp[i]);
		str[t]='0';
	}
	return 1;
}
string dfs(string str)
{
	string ans="",bak=str;
	bool f=1;
	for(int i=0;i<str.length();i++){
		if(str[i]!='0'){
			f=0;break;
		}
	}
	if(f) return "";
	bool ok=0;
	for(int i=0;i<10;i++){
		string tmp=mp[i];
		if(contain(str,tmp)){
			ans=dfs(str);
			ans=char('0'+i)+ans;
			ok=1;
			if(ans.find('-')!=-1){
				str=bak;
			}else break;
		}
	}
	if(!ok) return "-";
	return ans;
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		cin>>str;
		printf("Case #%d: ",cas);
		cout<<dfs(str);
		puts("");
	}
	
	
	return 0;
}
