#include "baz.h"

int main(){
	map<pair<char, char>, pair<char, int>> m;
	m[mp('1', '1')]=mp('1',1);
	m[mp('1', 'i')]=mp('i',1);
	m[mp('1', 'j')]=mp('j',1);
	m[mp('1', 'k')]=mp('k',1);

	m[mp('i', '1')]=mp('i',1);
	m[mp('i', 'i')]=mp('1',-1);
	m[mp('i', 'j')]=mp('k',1);
	m[mp('i', 'k')]=mp('j',-1);

	m[mp('j', '1')]=mp('j',1);
	m[mp('j', 'i')]=mp('k',-1);
	m[mp('j', 'j')]=mp('1',-1);
	m[mp('j', 'k')]=mp('i',1);

	m[mp('k', '1')]=mp('k',1);
	m[mp('k', 'i')]=mp('j',1);
	m[mp('k', 'j')]=mp('i',-1);
	m[mp('k', 'k')]=mp('1',-1);

	set<int> ok;
	int t, l, x;
	scanf("%d", &t);
	REP(bzn, t){
		scanf("%d%d", &l, &x);
		string s, ss;
		cin>>ss;
		REP(fn,x)s+=ss;
		//cout<<s<<endl;
		bool chocolate=0;
		ok.clear();

		char val='1';
		int zn=1;	
		for(int i=s.size()-1;i>=0;i--){
			auto tmp=m[mp(s[i], val)];
			val=tmp.fi;
			zn*=tmp.se;
			if(val=='k' && zn==1)ok.insert(i);
		}
		//for(auto it:ok)cout<<it<<"_";cout<<endl;
		char left='1';
		int znleft=1;
		for(int i=0;i<s.size();i++){
			auto tmp=m[mp(left,s[i])];
			left=tmp.fi;
			znleft*=tmp.se;
			if(left=='i' && znleft==1){
				//cout<<"left "<<i<<endl;
				char mid='1';
				int znmid=1;
				for(int j=i+1;j<s.size();j++){	
					auto tmp=m[mp(mid,s[j])];
					mid=tmp.fi;
					znmid*=tmp.se;
					//cout<<"mid "<<mid<<endl;
					if(mid=='j' && znmid==1 && ok.find(j+1)!=ok.end()){
						chocolate=1;goto HELL;
					}
				}
			}
		}
		HELL:
		if(chocolate){
			printf("Case #%d: YES\n", bzn+1);
		}
		else{
			printf("Case #%d: NO\n", bzn+1);
		}
	}
}