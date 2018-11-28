#include <queue>
#include <iostream>
#include <utility>
#include <vector>
#include <cstdio>
#include <functional>
using namespace std;

class Compare {
	public:
	bool operator()(pair<int,char> &a,pair<int,char> &b) {
		if(a.first==b.first)
			return (a.second<b.second);
		else
			return (a.first<b.first);
	}
};

int main() {
	ios_base::sync_with_stdio(0);

	pair<int,char> a,b,c;
	int t,i,j,N,p;
	cin>>t;

	for(i=1;i<=t;i++) {
		priority_queue<pair<int,char>,vector< pair<int,char> >,Compare> mypq;
		cin>>N;
		for(j=0;j<N;j++) {
			cin>>p;
			mypq.push(make_pair(p,j+'A'));
		}

		cout<<"Case #"<<i<<": ";
		while(!mypq.empty()) {
			if(mypq.size()==2) {
				a=mypq.top();
				mypq.pop();
				b=mypq.top();
				mypq.pop();
				cout<<a.second<<b.second<<" ";
				a.first--;
				b.first--;
				if(b.first!=0) {
					mypq.push(a);
					mypq.push(b);
				}
			}
			else {
				a=mypq.top();
				mypq.pop();
				b=mypq.top();
				mypq.pop();
				c=mypq.top();

				if(a.first==b.first) {
					if(a.first==c.first) {
						cout<<a.second<<" ";
						a.first--;
					}
					else {
						cout<<a.second<<b.second<<" ";
						a.first--;
						b.first--;
					}
				}
				else {
					cout<<a.second<<a.second<<" ";
					a.first-=2;
				}
				if(a.first!=0)
					mypq.push(a);
				if(b.first!=0)
					mypq.push(b);
			}
		}
		cout<<"\n";
	}
	

	return 0;
}