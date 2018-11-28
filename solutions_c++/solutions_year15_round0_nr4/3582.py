#include <iostream>
#include<cmath>

using namespace std;
 
int main() {
 
	int test,x,r,c;
	cin>>test;
 
	for(int j=1;j<=test;j++){
 
		cin>>x>>r>>c;
 
		if(x == 1){
			cout<<"Case #"<<j<<": GABRIEL"<<endl;
			continue;
		}
 
		char winnr = 'R';
		if(r>=x || c>=x){
		if((r*c) >= (x*((x+1)/2))){
		if((r*c)%x == 0){
 
		if ((r % 2) == 0 && (c % 2) == 0 && abs(r - c) == 2 && (x>=r) &&(x>=c)) {
         winnr = 'R';
         } else {
         winnr = 'G';
         }
		}
			}
		}
 
		if(winnr == 'R') cout<<"Case #"<<j<<": RICHARD"<<endl;
		else cout<<"Case #"<<j<<": GABRIEL"<<endl;
 
	}
 
	return 0;
}
