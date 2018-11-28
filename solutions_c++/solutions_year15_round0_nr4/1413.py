#include<bits/stdc++.h>
using namespace std;
main(){
	freopen("test.inp","r",stdin);
	freopen("test.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i = 1 ; i <= T ; i++){
		bool Richard_win = true;
		int x,r,c;
		scanf("%d %d %d",&x,&r,&c);
		if(r > c) swap(r , c);
		if(x == 1) Richard_win = false;
		else if(x == 2){
			if((r*c)%2 == 0) Richard_win = false; 
		}
		else if(x == 3){
			if( (r == 2 && c == 3) || (r == 3 && c == 4) || (r == 3 && c == 3)) Richard_win = false; 
		}
		else if(x == 4){
			if( (r == 3 && c == 4) || (r == 4 && c == 4) ) Richard_win = false;
		}
		cout<<"Case #"<<i<<": ";
		if(Richard_win) cout<<"RICHARD"<<'\n';
		else cout<<"GABRIEL"<<'\n';
	}
}
