#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cstring>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define VI vector<int>
#define PII pair<int,int>
#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define lint long long int

using namespace std;

lint gcd(lint a,lint b){
	return a%b==0 ? b : gcd(b,a%b);
}

int check(vector<string> dupa){
	set<string> kij;
	kij.insert("");
	FOR(i,0,dupa.size()){
		FOR(j,0,dupa[i].size()+1)
			kij.insert(dupa[i].substr(0,j));
	}
	return kij.size();
}


int main(){
	int z; scanf("%d",&z);
	int casenr=0;
	while(z--){
		casenr++;
		printf("Case #%d: ",casenr);
		int n,m;
		scanf("%d%d",&n,&m);
		vector<string> v;
		FOR(i,0,n){
			string s; cin>>s;
			v.pb(s);
		}
		int u =1 ; FOR(i,0,n) u*=m;
		int maxi = 0;
		int ile = 0;

		FOR(i,0,u){
			int mask = i;
			vector<string> dupa[10];
			VI color;
			FOR(j,0,n){
				color.pb(mask%m);
				dupa[mask%m].pb(v[j]);
				mask = mask/m;
			}
			bool flaga = true;
			FOR(i,0,m) if(dupa[i].size()==0) flaga = false;
			if(!flaga) continue;
			int res = 0;
			FOR(i,0,m){
				res+=check(dupa[i]);
			}
			if(res>maxi){
				maxi = res;
				ile = 1;
			}
			else if(res==maxi) ile++;
		}
		printf("%d %d\n",maxi,ile);


	}
	return 0;
}
  

