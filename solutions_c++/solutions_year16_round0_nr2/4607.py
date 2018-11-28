/*
 * Author:Õı”Ì«Ô(jywyq) 
 * Date:20160409
 */
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
using namespace std;
#define LL long long
char s[110];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("dataout.txt","w",stdout);
	int t,cas=0;
	cin>>t;
	while(t--){
		printf("Case #%d: ",++cas);
		scanf("%s",s);
		int len=strlen(s);
		int ans=0;
		for(int i=1;i<len;i++){
			if(s[i]!=s[i-1])ans++;
		}
		if(s[len-1]=='-')ans++;
		cout<<ans<<endl;
	}
}
