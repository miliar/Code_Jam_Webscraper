#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iostream>
#define PS system("pause");
using namespace std;
string s;
int n;
int sum=0;
string solve(string s){
	string ans;
	int n=s.size();
	int cur=0;
	while(cur<n){
		int L=cur;
		while(cur+1<n&&s[cur]==s[cur+1])
			cur++;
		int R=cur;
		sum+=((R-L+1))/2*10;
		if((R-L+1)%2==1)
			ans.push_back(s[L]);
		cur++;
	}
	return ans;
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int tt,cot=1;
	scanf("%d",&tt);
	while(tt--){
		cin>>s;
		sum=0;
		while(1){
			string tmp=s;
			s=solve(s);
			if(s.size()==tmp.size())
				break;
		}
		int cnt=s.size();
		sum+=cnt/2*5;
		printf("Case #%d: %d\n",cot++,sum);
	}
	//PS;
	return 0;
}