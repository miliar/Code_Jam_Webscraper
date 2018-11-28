#include<iostream>
#include<vector>
#include<stack>
#include<cstring>
#include<map>
#include<set>
#include<string>
#include<queue>
#include<algorithm>
#include<stdio.h>
#include<sstream>
#include<cmath>
#include<cctype>
#include<fstream>
#include<set>
#define mp(x,y) make_pair(x,y)
using namespace std;
string s1,s2;
int dp[103][103];
int rec(int i,int j){
	if(i==s1.size()-1 || j==s2.size()-1)
		if(i==s1.size()-1 && j==s2.size()-1)
			return 0;
		else{
			if(i==s1.size()-1){
				int c=0;
				while(s2[j]==s2[j-1]){
					j++;
					c++;
				}
				if(s2[j]=='0')
					return c;
				else
					return 500;



			}else
			{
				int c=0;
				while(s1[i]==s1[i-1]){
					i++;
					c++;
				}
				if(s1[i]=='0')
					return c;
				else
					return 500;

			}

		}
		
	if(dp[i][j]!=-1)
		return dp[i][j];
	int mn=500;
	if(s1[i]==s2[j])
		mn=min(mn,rec(i+1,j+1));//eq
	else{
		if(s1[i-1]==s1[i] )   //del s1
			mn=min(mn,1+rec(i+1,j));
		if(s2[j-1]==s2[j] )   //del s2
			mn=min(mn,1+rec(i,j+1));
		if( s1[i-1]==s2[j])  //add s1
			mn=min(mn,1+rec(i,j+1));
		if( s1[i]==s2[j-1])  //add s2
			mn=min(mn,1+rec(i+1,j));
		
	}
	return dp[i][j]=mn;

}
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.in","w",stdout);
	int n,t;
	scanf("%d",&t);
	for(int u=1;u<=t;++u){
		scanf("%d",&n);
		memset(dp,-1,sizeof dp);
		cin>>s1>>s2;
		s1='0'+s1+'0';
		s2='0'+s2+'0';
		printf("Case #%d: ",u);
		int res=rec(0,0);
		if(res<500)
			printf("%d\n",res);
		else
			printf("Fegla Won\n");


	}
	return 0;
}

