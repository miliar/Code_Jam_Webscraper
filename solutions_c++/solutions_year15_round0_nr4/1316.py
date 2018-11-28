#include <bits/stdc++.h>

using namespace std;

int min2(int a,int b){
	if(a<b) return a;
	else return b;
}

int max2(int a,int b){
	if(a<b) return b;
	else return a;
}




int main(){
	int t;
	cin>>t;
	for(int g=0;g<t;g++){
		int x, r, c;
		cin>>x>>r>>c;
		bool z = false;
		if(x == 1) z = true;
		if(x == 2 && r*c % 2 == 0) z = true;
		if(x == 3 && r*c % 3 == 0 && r*c > 3) z = true;
		if(x == 4 && r*c % 4 == 0 && r*c > 8) z = true;
		if(z) cout<<"Case #"<<g+1<<": "<<"GABRIEL"<<endl;
		else cout<<"Case #"<<g+1<<": "<<"RICHARD"<<endl; 
	}
}	