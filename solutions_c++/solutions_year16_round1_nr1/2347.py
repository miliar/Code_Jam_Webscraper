/*
By Tianyi Chen. All rights reserved.
Date: 2016-04-16
*/
#include<bits/stdc++.h>
using namespace std;
int T;
string t,anss;
deque<char>ans;
int main() {
	freopen("D:/publish/GCJ/2016-1A/A.in","r",stdin);
	freopen("D:/publish/GCJ/2016-1A/A.out","w",stdout);
	scanf("%d",&T);for (int _=1;_<=T;++_) {
		cin>>t;ans.clear();
		for (auto&&x:t)if (ans.empty())ans.push_back(x);
		else {
			if (x>=ans.front())ans.push_front(x);
			else ans.push_back(x);
		}
		printf("Case #%d: ",_);
		cout<<string(ans.begin(),ans.end())<<'\n';
	}
}