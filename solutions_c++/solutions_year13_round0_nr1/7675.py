#include <cstdio>
#include <iostream>
using namespace std;

#define SMALL
#define LARGE

int main() {
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small-attempt0.out", "wt", stdout);
	/*#ifdef SMALL
		freopen("A-small-practice.in", "rt", stdin);
		freopen("A-small-practice.out", "wt", stdout);
	#endif*/
	/*#ifdef LARGE
		freopen("A-large-practice.in", "rt", stdin);
		freopen("A-large-practice.out", "wt", stdout);
	#endif*/

	char a[4][4], c;
	int T;

	cin>>T;
	for(int i=1; i<=T; i++) {
		bool x=false, o=false, d=true;
		for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++) {
				cin>>c;
				a[j][k] = c;
			}
		}
		for(int j=0; j<4; j++) {
			if(a[j][0]=='X' || a[j][0]=='T') {
				if(a[j][1]=='X' || a[j][1]=='T') {
					if(a[j][2]=='X' || a[j][2]=='T') {
						if(a[j][3]=='X' || a[j][3]=='T') {
							x=true;
						}
					}
				}
			}
			else if(a[j][0]=='O' || a[j][0]=='T') {
				if(a[j][1]=='O' || a[j][1]=='T') {
					if(a[j][2]=='O' || a[j][2]=='T') {
						if(a[j][3]=='O' || a[j][3]=='T') {
							o=true;
						}
					}
				}
			}
		}
		for(int k=0; k<4; k++) {
			if(a[0][k]=='X' || a[0][k]=='T') {
				if(a[1][k]=='X' || a[1][k]=='T') {
					if(a[2][k]=='X' || a[2][k]=='T') {
						if(a[3][k]=='X' || a[3][k]=='T') {
							x=true;
						}
					}
				}
			}
			else if(a[0][k]=='O' || a[0][k]=='T') {
				if(a[1][k]=='O' || a[1][k]=='T') {
					if(a[2][k]=='O' || a[2][k]=='T') {
						if(a[3][k]=='O' || a[3][k]=='T') {
							o=true;
						}
					}
				}
			}
		}
		if(a[0][0]=='X' || a[0][0]=='T') 
			if(a[1][1]=='X' || a[1][1]=='T') 
				if(a[2][2]=='X' || a[2][2]=='T') 
					if(a[3][3]=='X' || a[3][3]=='T') 
						x=true;

		if(a[0][0]=='O' || a[0][0]=='T') 
			if(a[1][1]=='O' || a[1][1]=='T') 
				if(a[2][2]=='O' || a[2][2]=='T') 
					if(a[3][3]=='O' || a[3][3]=='T') 
						o=true;

		if(a[0][3]=='X' || a[0][3]=='T') 
			if(a[1][2]=='X' || a[1][2]=='T') 
				if(a[2][1]=='X' || a[2][1]=='T') 
					if(a[3][0]=='X' || a[3][0]=='T') 
						x=true;

		if(a[0][3]=='O' || a[0][3]=='T') 
			if(a[1][2]=='O' || a[1][2]=='T') 
				if(a[2][1]=='O' || a[2][1]=='T') 
					if(a[3][0]=='O' || a[3][0]=='T') 
						o=true;

		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				if(a[j][k]=='.')
					d=false;

		cout<<"Case #"<<i<<": ";
		if(x==true) cout<<"X won";
		else if(o==true) cout<<"O won";
		else if(x==false && o==false &&  d==true) cout<<"Draw";
		else cout<<"Game has not completed";
		cout<<endl;
	}
}