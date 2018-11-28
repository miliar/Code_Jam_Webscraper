#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<cstdio>
#include<cmath>
#include<set>
#include<string>
#include<ctype.h>
using namespace std;


bool try_(map<char,int> &th, map<int,int> &all) {
	int ok=1;
	if(th.find('o')!=th.end() && th['o']>0) {
		ok--;
		th['o']-=1;
		th['n']-=1;
		th['e']-=1;
		all[1]+=1;
		if(try_(th,all)) {ok+=2;} 
		else {
			th['o']+=1;
			th['n']+=1;
			th['e']+=1;
			all[1]-=1;
		}
	}
	if(th.find('r')!=th.end() && th['r']>0) {
		ok--;
		th['t']-=1;
		th['h']-=1;
		th['r']-=1;
		th['e']-=2;
		all[3]+=1;
		if(try_(th,all)) {ok+=2;} else {
			th['t']+=1;
			th['h']+=1;
			th['r']+=1;
			th['e']+=2;
			all[3]-=1;
		}
	}
	if(th.find('f')!=th.end() && th['f']>0) {
		ok--;
		th['f']-=1;
		th['i']-=1;
		th['v']-=1;
		th['e']-=1;
		all[5]+=1;
		if(try_(th,all)){ok+=2;} else {
			th['f']+=1;
			th['i']+=1;
			th['v']+=1;
			th['e']+=1;
			all[5]-=1;
		}
	}
	if(th.find('s')!=th.end() && th['s']>0) {
		ok--;
		th['s']-=1;
		th['e']-=2;
		th['v']-=1;
		th['n']-=1;
		all[7]+=1;
		if(try_(th,all)){ok+=2;} else {
			th['s']+=1;
			th['e']+=2;
			th['v']+=1;
			th['n']+=1;
			all[7]-=1;
		}
	}
	if(th.find('n')!=th.end() && th['n']>1) {
		ok--;
		th['n']-=2;
		th['i']-=1;
		th['e']-=1;
		all[9]+=1;
		if(try_(th,all)){ok+=2;} else {
			th['n']+=2;
			th['i']+=1;
			th['e']+=1;
			all[9]-=1;
		}
	}
	if(ok) return true;
	return false;
}


int main() {
	
	map<char,int> cnt;
	cnt['o']=3;
	cnt['n']=5;
	cnt['e']=9;
	cnt['t']=4;
	cnt['h']=2;
	cnt['r']=2;
	cnt['f']=2;
	cnt['i']=4;
	cnt['v']=2;
	cnt['s']=2;
	cnt['g']=1;
	cnt['w']=1;
	cnt['u']=1;
	cnt['x']=1;
	// g,w,u,x
	
	map<char,int> used;
	
	
	int T;
	cin>>T;
			cin.clear();
		cin.ignore(10000,'\n');
	for(int t=1;t<=T;t++) {
			map<int,int> all;
	
	map<char,int> th;
		
		string S;
		getline(cin,S);
		//S.tolower();
		for(std::string::iterator it = S.begin(); it != S.end(); ++it) {
			char c = *it;
			th[tolower(c)]+=1;
		}
		bool ok=true;
		while(ok) {
			ok=false;
			if(th.find('w')!=th.end() && th['w']>0) {
				th['t']-=1;
				th['w']-=1;
				th['o']-=1;
				all[2]+=1;
				ok=true;
			}
			if(th.find('u')!=th.end() && th['u']>0) {
				th['f']-=1;
				th['o']-=1;
				th['u']-=1;
				th['r']-=1;
				all[4]+=1;
				ok=true;
			}
			if(th.find('x')!=th.end() && th['x']>0) {
				th['s']-=1;
				th['i']-=1;
				th['x']-=1;
				all[6]+=1;
				ok=true;
			}
			if(th.find('g')!=th.end() && th['g']>0) {
				th['e']-=1;
				th['i']-=1;
				th['g']-=1;
				th['h']-=1;
				th['t']-=1;
				all[8]+=1;
				ok=true;
			}
			if(th.find('z')!=th.end() && th['z']>0) {
				th['z']-=1;
				th['e']-=1;
				th['r']-=1;
				th['o']-=1;
				all[0]+=1;
				ok=true;
			}
		}
		try_(th,all);
		cout<<"Case #"<<t<<": ";
		for(typeof(all.begin()) mi=all.begin();mi!=all.end();mi++) {		
			for(int x=0;x<mi->second;x++) {
				cout<<mi->first;
			}
		}
		cout<<endl;
	}
	return 0;
}
