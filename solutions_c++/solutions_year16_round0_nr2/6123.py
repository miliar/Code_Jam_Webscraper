#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int ntest;
string s;

void solve(int test){
	printf("Case #%d: ",test+1);
	getline(cin,s);
	stack<char> st;
	for(int i=0; s[i]; i++) st.push(s[i]);
	char cur = '+';
	int cnt=0;
	while(!st.empty()){
		if(st.top() == cur) st.pop();
		else{
			cur = st.top();
			st.pop();
			cnt ++;
		}
	}
	printf("%d\n",cnt);
}

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d\n",&ntest);	
	for(int i=0;i<ntest; i++){
		solve(i);
	}
	return 0;
}
	
	
	
