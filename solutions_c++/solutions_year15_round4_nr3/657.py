#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
using namespace std;


vector<string> split(const string &str,const string &sep){
	vector<string> res;
	string s;
	for(int i=0;i<str.size();i++){
		if(str.find(sep,i)==i){
			res.push_back(s);
			s.clear();
		}else{
			s+=str[i];
		}
	}
	res.push_back(s);
	return res;
}


map<string,int> id;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int testcase;
	cin>>testcase;
	rep(_,testcase){
		
		int n;
		cin>>n;
		cin.ignore();
		vector<vector<int> > v;
		rep(i,n){
			string s;
			vector<string> vs;
			getline(cin,s);
			vs=split(s," ");
			v.push_back(vector<int>());
			rep(j,vs.size()){
				if(id.find(vs[j])==id.end()){
					int m=id.size();
					v[i].push_back(m);
					id[vs[j]]=m;
				}else v[i].push_back(id[vs[j]]);
			}
		}
		int ans=INF;
		rep(i,1<<n-2){
			vector<int> lang(id.size()+1,0);
			int bs=i<<2|1;
			rep(j,n){
				int bf;
				bf=(bs>>j&1)+1;
				rep(k,v[j].size()){
					lang[v[j][k]]|=bf;
				}
			}
			int c=0;
			rep(j,lang.size()){
				if(lang[j]==3)c++;
			}
			ans=min(ans,c);
		}
		cout<<"Case #"<<_+1<<": ";
		cout<<ans<<endl;
	}
	return 0;
}