#include<iostream>
using namespace std;

int t,x,r,c,bufor;	
	
int main(){
	cin>>t;
	for(int i = 0; i < t; i++){
		cin>>x>>r>>c;
		
		cout<<"Case #"<<i+1<<": ";
		
		if((r*c) % x != 0)cout<<"RICHARD"<<endl;
		else{
			if(r < c){
				bufor = r;
				r = c;
				c = bufor;
			}
			if(((x >= 3) && (c == 1)) || (x == 4 && r == 2 && c == 2) || (x == 4 && r == 4 && c == 2))cout<<"RICHARD"<<endl;
			else cout<<"GABRIEL"<<endl;
		}
	}

return 0;
}
