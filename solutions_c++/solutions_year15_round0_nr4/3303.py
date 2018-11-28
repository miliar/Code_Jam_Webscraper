#include <bits/stdc++.h>
using namespace std;
string f(int x,int r,int c){
	if((x>r && x>c) || (r*c)%x) return "RICHARD";
	if(x==1 || x==2) return "GABRIEL";
	if((r*c)/x<(x-1)) return "RICHARD";
	return "GABRIEL";
}
int main(){
	freopen("D-small-attempt0.in", "r", stdin);
  	freopen("OUTD.txt", "w", stdout);
	int t,x,r,c;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>x>>r>>c;
		cout<<"Case #"<<k<<": "<<f(x,r,c)<<endl;
	}
	return 0;
}
/*
GABRIEL
RICHARD
*/