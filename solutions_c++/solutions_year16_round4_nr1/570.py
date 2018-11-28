/*
 * Author:Õı”Ì«Ô(jywyq) 
 * Date:20160528
 */
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
using namespace std;
#define LL long long
char to[1000];
int N,R,P,S;
int r,s,p;
string dfs(int l,int r,char crt){
	if(l==r){
		char ss[2];
		ss[0]=crt;ss[1]='\0';
		string s=ss;
		//cout<<s<<endl;
		return s;
	}
	int mid=(l+r)>>1;
	string s1=dfs(l,mid,to[crt]);
	string s2=dfs(mid+1,r,crt);
	if(s1<=s2)return s1+s2;
	else return s2+s1;
}
bool check(string ans){
	r=s=p=0;
	for(int i=0;i<(1<<N);i++){
		if(ans[i]=='R')r++;
		if(ans[i]=='S')s++;
		if(ans[i]=='P')p++;
	}
	return r==R&&s==S&&p==P;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("dataout.txt","w",stdout);
	to['R']='S';to['S']='P';to['P']='R';
	int t,cas=0;
	cin>>t;
	while(t--){
		bool flag=1;
		cin>>N>>R>>P>>S;
		string s=dfs(1,1<<N,'P');
		//cout<<s<<endl;
		if(check(s)){
			printf("Case #%d: ",++cas);
			cout<<s<<endl;
			flag=0;
		}
		s=dfs(1,1<<N,'R');
		//cout<<s<<endl;
		if(check(s)){
			printf("Case #%d: ",++cas);
			cout<<s<<endl;
			flag=0;
		}
		s=dfs(1,1<<N,'S');
		//cout<<s<<endl;
		if(check(s)){
			printf("Case #%d: ",++cas);
			cout<<s<<endl;
			flag=0;
		}
		if(flag)printf("Case #%d: IMPOSSIBLE\n",++cas);
	}
}
