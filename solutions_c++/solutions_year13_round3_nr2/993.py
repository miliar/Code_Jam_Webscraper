#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int T,x,y;
int main(){
 	freopen("b.in","rt",stdin);
 	freopen("b.out","wt",stdout);
 	cin>>T;	
 	for(int t=1;t<=T;t++) {
 	 	cin>>x>>y;
 	 	string s="";
 	 	while(y) {
 	 		if(y>0) {
 	 			s+="SN"; 
 	 			y--;
 	 		} else {
 	 			s+="NS";
 	 			y++;
 	 	   }
 	 	}
 	 	while(x) {
 	 	 	if(x>0) {
 	 	 	    s+="WE";
 	 	 	    x--;
 	 	 	} else {
 	 	 	    s+="EW";
 	 	 	    x++;
 	 	 	}
 	 	}
 	 	cout<<"Case #"<<t<<": "<<s<<endl;
 	}
 	return 0;
}