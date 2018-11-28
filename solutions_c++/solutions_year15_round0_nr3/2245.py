#include <bits/stdc++.h>
using namespace std;
map<pair<char,char> ,pair<char,int> > m;
map <char,int> l;

int main(){
	ios::sync_with_stdio(false); 
    freopen("a.txt","r",stdin);
    freopen("out2.txt","w",stdout);
	int t;
	cin >> t;
	l['1']=0;
	l['i']=1;
	l['j']=2;
	l['k']=3;
	m[{'i','i'}]={'1',1};
	m[{'i','j'}]={'k',0};
	m[{'i','k'}]={'j',1};
	m[{'i','1'}]={'i',0};
	m[{'j','i'}]={'k',1};
	m[{'j','j'}]={'1',1};
	m[{'j','k'}]={'i',0};
	m[{'j','1'}]={'j',0};
	m[{'k','i'}]={'j',0};
	m[{'k','j'}]={'i',1};
	m[{'k','k'}]={'1',1};
	m[{'k','1'}]={'k',0};
	m[{'1','i'}]={'i',0};
	m[{'1','j'}]={'j',0};
	m[{'1','k'}]={'k',0};
	m[{'1','1'}]={'1',0};
	for(int tt=1;tt<=t;tt++){
		cout << "Case #" << tt << ": ";
		long long ll,x;
		cin >> ll >> x;
		string s;
		string ss;
		cin >> s;
		ss = s+s+s+s;
		int sg=0;
		char c='1';
		for(size_t i=0;i<s.length();i++){
			pair<char,int> temp = m[{c,s[i]}];
			c = temp.first;
			if(temp.second==1) sg = temp.second-sg;
		}
		int flag=0;
		if((c=='1') && (sg==1) && (x%2)==1) flag=1;
		if((c!='1') && ((x%4)==2)) flag=1;
		if(flag==0){
			cout << "NO\n";
			continue;
		}
		
		int a1[8];
		int a2[8];
		for(int i=0;i<8;i++) a1[i]=-1,a2[i]=-1;
		a1[0]=0;a2[0]=0;
		sg=0;
		c='1';
		for(size_t i=0;i<ss.length();i++){
			pair<char,int> temp = m[{c,ss[i]}];
			c = temp.first;
			if(temp.second==1) sg = temp.second-sg;
			if(a1[4*sg + l[temp.first]]==-1) a1[4*sg + l[temp.first]]=i+1;
		}
		int s1=-1;
		if(a1[1]!=-1) s1=a1[1];
		else{
			cout << "NO\n";
			continue;
		}
		c='1';
		sg=0;
		for(int i=ss.length()-1;i>=0;i--){
			pair<char,int> temp = m[{ss[i],c}];
			c = temp.first;
			if(temp.second==1) sg = temp.second-sg;
			if(a2[4*sg + l[temp.first]]==-1) a2[4*sg + l[temp.first]]=ss.length()-i;
		}
		int s2=-1;
		if(a2[3]!=-1) s2=a2[3];
		else{
			cout << "NO\n";
			continue;
		}
		if(s1+s2<ll*x) cout << "YES\n";
		else cout << "NO\n";
	}
	return 0;
}
