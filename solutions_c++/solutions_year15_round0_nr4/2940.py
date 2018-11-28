#include <iostream>
using namespace std;
 
int main() {
 
	int test,x,r,c;
	cin>>test;
 
	for(int t=1;t<=test;t++){
 
		cin>>x>>r>>c;
 
		if(x == 1){
			cout<<"Case #"<<t<<": GABRIEL\n";
			continue;
		}
 
		char winner = 'R';
		if(r>=x || c>=x){
			if((r*c) >= (x*((x+1)/2))){
				if((r*c)%x == 0){
 
					if ((r % 2) == 0 && (c % 2) == 0 && abs(r - c) == 2 && (x>=r) &&(x>=c)) {
                        winner = 'R';
                    } else {
                        winner = 'G';
                    }
				}
			}
		}
 
		if(winner == 'R') cout<<"Case #"<<t<<": RICHARD\n";
		else cout<<"Case #"<<t<<": GABRIEL\n";
 
	}
 
	return 0;
}