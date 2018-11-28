#include<iostream>
#include<algorithm>
#include<deque>
#include<string>
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;cin>>t;
	for(int x=1;x<=t;x++){
		string s;cin>>s;
		deque<char> dq;
		char f=s[0];
		dq.push_front(s[0]);
		for(int i=1;i<s.length();i++){
			if(s[i]>=f){
				dq.push_front(s[i]);
				if(s[i]>f)f=s[i];
			}
			else{
				dq.push_back(s[i]);
			}
		}
		cout<<"Case #"<<x<<": ";
		for(int i=0;i<s.size();i++){
			cout<<dq[i];
		}
		cout<<endl;
	}
	return 0;
}

