#include<iostream>
#include<cstdio>

using namespace std;

int main() {

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T;
	cin>>T;

	for(int t=1 ; t<=T ; t++) {	
		int X,R,C;
		cin>>X>>R>>C;

		bool chk=true;

		if(R<C) { int tmp=R; R=C; C=tmp; }

		if(X==2) {
			if(R==1) chk=false;
			if(R==3) {
				if(C==1) chk=false;
				else if(C==3) chk=false;
			}
		}
		else if(X==3) {
			if(R<=2) chk=false;
			else if(R==3) {
				if(C==1) chk=false;
			}
			else if(R==4) {
				if(C==1 || C==2) chk=false;
				if(C==4) chk=false;
			}			
		}
		else if(X==4) {
			if(R<=3) chk=false;
			else {
				if(C<=2) chk=false;
			}
		}

		cout<<"Case #"<<t<<": ";
		if(chk) cout<<"GABRIEL\n";
		else cout<<"RICHARD\n";
	}

	return 0;
}