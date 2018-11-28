#include<bits/stdc++.h>
using namespace std;
queue<int> q;
int t;
int tail;
int main(){
	std::ios::sync_with_stdio(false);
	cin >> t;
	for(int t1=1;t1<=t;t1++){
		string s;
		cin >> s;
		tail=0;
		
		bool now_min=true;
		if(s[0]=='-') now_min=false;
		for(int n1=0;n1<s.length();n1++){
			if(now_min&&s[n1]=='+'){
				now_min=false;
				q.push(1);
				continue;
			}
			if(!now_min&&s[n1]=='-'){
				now_min=true;
				tail++;
				q.push(0);
			}
		}
		int ans=0;
		while(!q.empty()&&tail){
			int temp=q.front();
			if(!temp){
				tail--;
			}
			q.pop();
			ans++;
		}
		while(!q.empty()) q.pop();
		cout<<"Case #"<<t1<<": "<<ans<<"\n";
	}
}
