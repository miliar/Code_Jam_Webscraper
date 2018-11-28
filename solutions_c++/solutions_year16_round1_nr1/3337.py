#include <iostream>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;
deque<char>q;
int main(){
	int cases;
	cin>>cases;
	int tc=1;
	while(cases--){
		string s;
		cin>>s;
		q.clear();
		q.push_back(s[0]);
		for(int i=1;i<s.size();i++){
			if(q.front()<=s[i])q.push_front(s[i]);
			else q.push_back(s[i]);
		}
		cout<<"Case #"<<tc++<<": ";
		for(char u:q)cout<<u;
		cout<<"\n";
	}
}
