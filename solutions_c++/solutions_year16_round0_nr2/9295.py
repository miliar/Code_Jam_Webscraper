#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair 
#define sz(v) ((int)v.size())
#define REP(i,s,f) for(int i = s; i < f; i++)
#define fst first
#define snd second
string s;
vector<int>v;
int ans;

int ok(){
	REP(i,0,sz(v)){
		if(v[i]==0)return 0;
	}
	return 1;
}

void go(){
	int pos,flag;
	flag=v[0];
	while(1){
		if(ok()) return;
		ans++;
		for(pos=0;pos<sz(v);pos++){
			if(v[pos]!=flag){
				if(flag==1) flag=0;
				else flag=1;
				//pos=i;
				break;
			}
		}
		REP(i,0,pos){
			if(v[i]==1) v[i]=0;
			else v[i]=1;
		}
	}
}

int main(){
	int t,cases;
	cin>>t;
	cases=1;
	REP(i,0,t){
		ans=0;
		v.clear();
		cin>>s;
		REP(j,0,sz(s)){
			if(s[j]=='+') v.pb(1);
			else v.pb(0);
		}
		go();
		cout<<"Case #"<<cases<<": "<<ans<<endl;
		cases++;
	}
	return 0;
}
