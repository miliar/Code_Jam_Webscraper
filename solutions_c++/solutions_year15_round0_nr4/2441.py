#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int num[1005];

int main(){
	ofstream out("D-small-attempt2.out");
   	ifstream in("D-small-attempt2.in");
	int t,x,r,c,o=1;
	in>>t;
	while(t--){
		in>>x>>r>>c;
		if(r==1 && c==1){
			if(x==1) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==1 && c==2){
			if(x==1 || x==2) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==1 && c==3){
			if(x==1) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==1 && c==4){
			if(x==1 || x==2) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		//
		if(r==2 && c==1){
			if(x==1 || x==2) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==2 && c==2){
			if(x==1 || x==2) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==2 && c==3){
			if(x==1 || x==2 || x==3) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==2 && c==4){
			if(x==1 || x==2) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		//
		if(r==3 && c==1){
			if(x==1) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==3 && c==2){
			if(x==1 || x==2 || x==3) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==3 && c==3){
			if(x==1 || x==3) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==3 && c==4){
			if(x==1 || x==2 || x==3 || x==4) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		//
		if(r==4 && c==1){
			if(x==1 || x==2) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==4 && c==2){
			if(x==1 || x==2) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==4 && c==3){
			if(x==1 || x==2 || x==3 || x==4) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
		if(r==4 && c==4){
			if(x==1 || x==2 || x==4) out<<"Case #"<<o++<<": GABRIEL"<<endl;
			else out<<"Case #"<<o++<<": RICHARD"<<endl;
		}
	}
	out.close();
   	in.close();
	return 0;
}
