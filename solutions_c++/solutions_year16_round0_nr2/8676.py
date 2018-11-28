#include <iostream>
#include <fstream>
using namespace std;

ifstream in ("b.in");
ofstream out ("b.out");

//string p[300];
int t;

int maneuver(string p){
	if(p=="")
		return 0;
	int l=p.length()-1;
	while(l>0 && p[l]==p[l-1] ){
		l--;
	}
	return maneuver(p.substr(0,l))+1;
}

int main(){
	in>>t;
	for(int x=0;x<t;x++){
		string p;
		in>>p;
		int l=p.length()-1;
		if(p[l]=='+')
			while(l>0 && p[l]==p[l-1] ){
				l--;
			}
		else
			l++;
		out<<"Case #"<<(x+1)<<": "<<maneuver( p.substr(0, l ) )<<endl;		
	}
	
	
}

