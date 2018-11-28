#include <iostream>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>

#define LL long long 

using namespace std;
const int maxn = 1e4+5;
const int inf = 1e9+7;


map<char, pair<char, char> > mp; 
string ansr[15], ansp[15], anss[15];
pair<int,int> cntr[15], cntp[15], cnts[15];
string gao(string from){
	string res; res.clear();
	int n = from.size();

	for(int j=0;j<n;j++){
		pair<char, char> v = mp[ from[j] ];
		res.push_back( v.first );
		res.push_back( v.second );
	}
	return res;
}


pair<int,int> getcnt(string a){
	int n = a.size();
	int r = 0, p = 0;
	for(int i=0;i<n;i++){
		if ( a[i]=='R' ) r++;
		if ( a[i]=='P' ) p++;
	}
	return make_pair(r, p);
}


string mycmp(string s, int u1, int u2){
	int n = u2 - u1; bool flag = true;
	for(int i=0;i<n;i++){
		if ( s[u1+i]>s[u2+i] ){
			flag = false;
		}
	}
	if ( !flag ){
		for(int i=0;i<n;i++){
			swap(s[u1+i], s[u2+i]);
		}
	}
	return s;
}
string mysort(string s){
	int n = s.size();
	for(int i=1;i<n;i=i*2){
		for(int j=0;j<n;j+=i+i){
			s = mycmp(s, j, j+i);
		}
	}
	return s;
}
void prework(){
	mp['R'] = make_pair('R', 'S');
	mp['P'] = make_pair('P', 'R');
	mp['S'] = make_pair('P', 'S');

	ansr[0] = "R";
	ansp[0] = "P";
	anss[0] = "S";
	for(int i=1;i<=12;i++){
		ansr[i] = gao(ansr[i-1]);
		ansp[i] = gao(ansp[i-1]);
		anss[i] = gao(anss[i-1]);
	}

	for(int i=0;i<=12;i++){
		cntr[i] = getcnt(ansr[i]);
		cntp[i] = getcnt(ansp[i]);
		cnts[i] = getcnt(anss[i]);
		
		ansr[i] = mysort(ansr[i]);
		ansp[i] = mysort(ansp[i]);
		anss[i] = mysort(anss[i]);
		
	}
}


int n, r, p, s;
bool judge(pair<int,int> v){
	if ( r==v.first && p==v.second )
		return true;
	else 
		return false;
}

int main(){

	prework();

	int T; scanf("%d", &T);
	for(int it=1;it<=T;it++){

		printf("Case #%d: ", it);
		scanf("%d%d%d%d", &n, &r, &p, &s);

		vector<string> ans; ans.clear();
		if ( judge(cntr[n]) ) ans.push_back( ansr[n] );
		if ( judge(cntp[n]) ) ans.push_back( ansp[n] );
		if ( judge(cnts[n]) ) ans.push_back( anss[n] );
		
		if ( ans.size()==0 ) {
			printf("IMPOSSIBLE\n");
		}
		else {
			sort(ans.begin(), ans.end());
			printf("%s\n", ans[0].c_str() );
		}

	}	

	return 0;
}

