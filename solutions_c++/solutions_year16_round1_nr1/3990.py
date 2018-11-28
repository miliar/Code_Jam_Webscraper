#include<bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	cin.ignore();
	for(int j=1;j<=t;j++){
		string s;
		cin>>s;
		deque<char> q;
		q.push_back(s[0]);
		for(int i=1;i<s.length();i++){
			if(s[i]<q.front())
				q.push_back(s[i]);
			else
				q.push_front(s[i]);
		}
		printf("Case #%d: ",j);
		for(auto it=q.begin();it!=q.end();it++)
			cout<<*it;
		cout<<endl;
	}
	return 0;
}
