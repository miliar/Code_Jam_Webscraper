#include <iostream>
#include <cstdio>
using namespace std;

int main(void) {
	int t; scanf("%d\n", &t);
	for(int cc=1;cc<=t;cc++) {
		int x, r, c;
		cin>>x>>r>>c;
		string winner="GABRIEL";
		if(r>c) {int t=c; c=r; r=t;}
		cerr<<"  r = "<<r<<" && c = "<<c<<" r > c ? "<<(r>c)<<endl;
		/*                case (1,_)                  */
		if(r==1&&c==1) {
			if(x>1) winner="RICHARD";
		} else if(r==1&&c==2) {
			if(x==3||x==4) winner="RICHARD";
		} else if(r==1&&c==3) {
			if(x!=1) winner="RICHARD";
		} else if(r==1&&c==4) {
			if(x==3||x==4) winner="RICHARD";
		}  /*               case (2,_)                   */
		else if(r==2&&c==2) {
			if(x==3||x==4) winner="RICHARD";
		} else if(r==2&&c==3) {
			if(x==4) winner="RICHARD";
		} else if(r==2&&c==4) {
			if(x==3||x==4) winner="RICHARD";
		}  /*               case (3,_)                   */
		else if(r==3&&c==3) {
			if(x==2||x==4) winner="RICHARD";
		} else if(r==3&&c==4) {
			//winner="RICHARD";
		}  /*               case (4,_)                   */
		else if(r==4&&c==4) {
			if(x==3) winner="RICHARD";
		}
		printf("Case #%d: %s\n", cc, winner.c_str());
	}
}