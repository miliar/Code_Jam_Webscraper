#include <bits/stdc++.h>
using namespace std;
int m[26],n;
int main(){
	int test,T,i,j;
	cin>>T;
	for(test=1;test<=T;++test){
		cin>>n;
		for(i=0;i<n;++i)cin>>m[i];
		cout<<"Case #"<<test<<": ";
		vector<pair<int,int> >ret;
		priority_queue<pair<int,int> >q;
		for(i=0;i<n;++i)
			q.push(make_pair(m[i],i));
		pair<int,int> top,x;
		int u,v;
		while(1){
			int maxi=0,cc=0;
			for(i=0;i<n;++i){
				if(maxi<m[i]){
					maxi = m[i];u= i;
				}
			}
			if(maxi==0)break;
			//cout<<maxi<<endl;
			m[u]--;int sm=0;
			for(i=0;i<n;++i){
				if(sm<=m[i]){
					if(sm==m[i])++cc;
					else{
					sm = m[i],v= i;cc=1;
					}
				}
			}
			if(sm==maxi && cc==1)
				m[v]--,ret.push_back(make_pair(u,v));
			else
				ret.push_back(make_pair(u,-1));
		}
		for(i=0;i<ret.size();++i){
			cout<<char('A'+ret[i].first);
			if(ret[i].second>=0)cout<<char('A'+ret[i].second);cout<<" ";
		}
		cout<<endl;
	}
}
