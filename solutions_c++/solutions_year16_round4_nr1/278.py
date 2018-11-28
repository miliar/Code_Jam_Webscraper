#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
#define PS system("pause");
using namespace std;
int n,R,P,S;
string fi;
string dfs(string &a,int L,int R){
	string ans="";
	if(L==R){
		ans.push_back(a[L]);
		return ans;
	}
	int m=L+(R-L+1)/2-1;
	string ans1=dfs(a,L,m);
	string ans2=dfs(a,m+1,R);
	if(ans1<ans2)
		return ans1+ans2;
	else
		return ans2+ans1;
}
string doit(vector<int>a){
	string ans="";
	for(auto x:a){
		if(x==1)
			ans.push_back('P');
		else if(x==2)
			ans.push_back('R');
		else
			ans.push_back('S');
	}
	string res=dfs(ans,0,(1<<n)-1);
	return res;
}
void update(string &T){
	int p=0,r=0,s=0;
	for(auto x:T){
		if(x=='P')
			p++;
		else if(x=='R')
			r++;
		else
			s++;
	}
	if(p==P&&R==r&&S==s){
		if((int)fi.size()==0)
			fi=T;
		else if(T<fi)
			fi=T;
	}
}
void solve(){
	vector<int>cur,tmp;
	for(int i=1;i<=3;i++){
		cur.clear();
		cur.push_back(i);
		for(int j=1;j<=n+1;j++){
			tmp.clear();
			for(int k=0;k<(int)cur.size();k++){
				if(cur[k]==1){
					tmp.push_back(1);
					tmp.push_back(2);
				}
				else if(cur[k]==2){
					tmp.push_back(2);
					tmp.push_back(3);
				}
				else{
					tmp.push_back(3);
					tmp.push_back(1);
				}
			}
			cur=tmp;
		}
		string S=doit(cur);
		update(S);
	}
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	int cot=1;
	while(tt--){
		fi="";
		scanf("%d%d%d%d",&n,&R,&P,&S);
		solve();
		if((int)fi.size()==0)
			printf("Case #%d: IMPOSSIBLE\n",cot++);
		else{
			printf("Case #%d: ",cot++);
			cout<<fi<<endl;
		}
	}
	//PS;
	return 0;
}
