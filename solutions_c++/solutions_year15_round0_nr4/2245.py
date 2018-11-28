#include <bits/stdc++.h>
using namespace std;
int main(){
	int test;
	scanf("%d",&test);
	for (int k = 1; k <= test; k++) {
		int x,r,c;
		cin>>x>>r>>c;
		if(r>c) swap(r,c);
		bool flag=true;
		if(x==2){
			if(r==1 && c==1) flag=false;
			if(r==1 && c==3) flag=false;
			if(r==3 && c==3) flag=false;
		}
		if(x==3){
			if(r==1 && c==1) flag=false;
			if(r==1 && c==2) flag=false;
			if(r==1 && c==3) flag=false;
			if(r==1 && c==4) flag=false;

			if(r==2 && c==2) flag=false;
			if(r==2 && c==4) flag=false;

			if(r==4 && c==4) flag=false;
		}
		if(x==4){
			if(r==1 && c==1) flag=false;
			if(r==1 && c==2) flag=false;
			if(r==1 && c==3) flag=false;
			if(r==1 && c==4) flag=false;

			if(r==2 && c==2) flag=false;
			if(r==2 && c==3) flag=false;
			if(r==2 && c==4) flag=false;

			if(r==3 && c==3) flag=false;
		}
		if(flag) cout<<"Case #"<<k<<": GABRIEL\n";
		else cout<<"Case #"<<k<<": RICHARD\n";
	}
}