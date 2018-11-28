#include <iostream>
#include <string>
#include <vector>

#define ll long long
using namespace std;



void recurstr(string st,int &N,int &J,vector< pair<string, vector<ll> > > &foo) {
	if(st.length()==N-1) {
		if(J==0)
			return;
		st.push_back('1');
		vector<ll> ls;
		ll num,k,i;
		bool fg;
		for(i=2;i<=10;i++) {			
			num=stol(st,0,i);
			fg=0;
			for(k=2;k*k<=num;k++) {
				if(num%k==0) {
					fg=1;
					break;
				}
			}
			if(!fg)
				break;
			else
				ls.push_back(k);
		}
		if(fg) {
			foo.push_back(make_pair(st,ls));
			J--;
		}
		return;
	}
	else {
		if(J==0)
			return;
		recurstr(st+'0',N,J,foo);
		recurstr(st+'1',N,J,foo);
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	int T,i,N,J,k,len,l;
	vector<ll> ls;
	vector< pair<string, vector<ll> > > foo;
	cin>>T;

	for(i=1;i<=T;i++) {
		cin>>N>>J;
		string st;
		st.push_back('1');
		recurstr(st,N,J,foo);
		cout<<"Case #"<<i<<": \n";
		len=foo.size();
		for(k=0;k<len;k++) {
			cout<<foo[k].first<<" ";
			ls=foo[k].second;
			for(l=0;l<9;l++)
				cout<<ls[l]<<" ";
			cout<<"\n";
		}
		foo.clear();
	}
	return 0;
}