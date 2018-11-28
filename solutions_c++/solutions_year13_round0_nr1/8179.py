#include<iostream>
#include<cstring>
using namespace std;
int main() {
	int t,cx,cO,ct,check;
	cin>>t;
	char in[t][20];
	for(int i=0;i<t;i++)
		for(int j=0;j<16;j++)
			cin>>in[i][j];
	for(int i=0;i<t;i++) {
		check=0;
		for(int j=0;j<13;j=j+4) {
			cx=cO=ct=0;
			for(int k=j;k<j+4;k++) {
				if(in[i][k]=='X') cx++;
				if(in[i][k]=='O') cO++;
				if(in[i][k]=='T') ct++;
			}
			if(cx==4||(cx==3&&ct==1)) {
				cout<<"Case #"<<(i+1)<<": "<<"X won"<<endl;
				check=1;
				break;
			}
			if(cO==4||(cO==3&&ct==1)) {
				cout<<"Case #"<<(i+1)<<": "<<"O won"<<endl;
				check=1;
				break;
			}
		}
		if(check==1) continue;
		for(int j=0;j<4;j++) {
			cx=cO=ct=0;
			for(int k=j;k<j+13;k=k+4) {
				if(in[i][k]=='X') cx++;
				if(in[i][k]=='O') cO++;
				if(in[i][k]=='T') ct++;
			}
			if(cx==4||(cx==3&&ct==1)) {
				cout<<"Case #"<<(i+1)<<": "<<"X won"<<endl;
				check=1;
				break;
			}
			if(cO==4||(cO==3&&ct==1)) {
				cout<<"Case #"<<(i+1)<<": "<<"O won"<<endl;
				check=1;
				break;
			}
		}
		if(check==1) continue;
		cx=cO=ct=0;
		for(int k=0;k<16;k=k+5) {
				if(in[i][k]=='X') cx++;
				if(in[i][k]=='O') cO++;
				if(in[i][k]=='T') ct++;
			}
			if(cx==4||(cx==3&&ct==1)) {
				cout<<"Case #"<<(i+1)<<": "<<"X won"<<endl;
				check=1;
			}
			if(cO==4||(cO==3&&ct==1)) {
				cout<<"Case #"<<(i+1)<<": "<<"O won"<<endl;
				check=1;
		}
		if(check==1) continue;
		cx=cO=ct=0;
		for(int k=3;k<13;k=k+3) {
				if(in[i][k]=='X') cx++;
				if(in[i][k]=='O') cO++;
				if(in[i][k]=='T') ct++;
		}
		if(cx==4||(cx==3&&ct==1)) {
			cout<<"Case #"<<(i+1)<<": "<<"X won"<<endl;
			check=1;
		}
		if(cO==4||(cO==3&&ct==1)) {
			cout<<"Case #"<<(i+1)<<": "<<"O won"<<endl;
			check=1;
		}
		if(check==1) continue;
		for(int j=0;j<16;j++)
			if(in[i][j]=='.') check++;
		if(check>0)
		cout<<"Case #"<<(i+1)<<": "<<"Game has not completed"<<endl;
		else
		cout<<"Case #"<<(i+1)<<": "<<"Draw"<<endl;
	}			
	return 0;	
}
