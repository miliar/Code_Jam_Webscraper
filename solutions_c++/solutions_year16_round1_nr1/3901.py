#include <bits/stdc++.h>
using namespace std;

int dp[1005][200][200];
string s;
int n;
string answer;


bool findLast(int i, int first, int last){
	if(i==n){
		answer = "";
		return true;
	}
	if(dp[i][first][last]!=-1)
		return dp[i][first][last];

	string temp1(1,s[i]);
	temp1=(temp1+(char)first)+(char)last;
	string temp2(1,(char)first);
	temp2=(temp2+(char)last)+s[i];

	if(temp1 > temp2){
		if(findLast(i+1,s[i],last)){
			answer = s[i]+answer;
			return dp[i][first][last]=true;
		}
		if(findLast(i+1, first, s[i])){
			answer = answer+s[i];
			return dp[i][first][last]=true;
		}
	}
	else{
		if(findLast(i+1, first, s[i])){
			answer = answer+s[i];
			return dp[i][first][last]=true;
		}	
		if(findLast(i+1,s[i],last)){
			answer = s[i]+answer;
			return dp[i][first][last]=true;
		}
	}
	return dp[i][first][last]=false;
}


int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cc=1, t;
	cin>>t;
	while(t--){
		memset(dp,-1,sizeof(dp));
		cout<<"Case #"<<cc++<<": ";
		cin>>s;
		n = s.length();
		//findLast(0,'#','#');
		answer = "";
		for(int i=0;i<n;i++){
			if(answer+s[i] > s[i]+answer){
				answer = answer+s[i];
			}
			else answer = s[i]+answer;
		}
		cout<<answer<<endl;
	}


	return 0;
}