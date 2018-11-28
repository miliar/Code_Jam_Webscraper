// -*- compile-command: "g++ -g -Wall -Wextra -DLOCAL -std=c++11 -D_GLIBCXX_DEBUG a.cpp -oa && ./a " -*-
#include <bits/stdc++.h>
using namespace std;

#define vc vector
#define pb push_back
#define pr pair
#define fi first
#define se second
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
#define f(i,n) for(int i=0;i<(n);i++)
#define fv(i,v) f(i,sz(v))
using LL=long long;
using str=string;

void solve(){
	int r,c;
	cin>>r>>c;
	vc<str> mp(r);
	f(i,r) cin>>mp[i];
	vc<bool> ch(r,0);
	int res=0;
	f(i,r){
		f(j,c){
			if(mp[i][j]=='.') continue;
			bool ok[4]={0,0,0,0};
			f(k,4){
				int dx=(k==0)-(k==2),dy=(k==1)-(k==3);
				for(int x=i+dx,y=j+dy;0<=x&&x<r&&0<=y&&y<c;x+=dx,y+=dy){
					if(mp[x][y]=='.') continue;
					ok[k]=1;
					break;
				}
			}
			bool okx=0;
			f(k,4) if(ok[k]) okx=true;
			if(!okx){ cout<<"IMPOSSIBLE\n"; return; }
			int theok=-1;
			switch(mp[i][j]){
			case 'v': theok=0; break;
			case '>': theok=1; break;
			case '^': theok=2; break;
			case '<': theok=3; break;
			}
			if(!ok[theok]) res++;
		}
	}
	cout<<res<<'\n';
}

int main(){
	ios::sync_with_stdio(0),cin.tie(0);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		solve();
	}
}
