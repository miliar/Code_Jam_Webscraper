#include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[]) {
	freopen( "input_s.txt", "r", stdin );
	freopen( "output_s.txt", "w", stdout );
	int cases;
	
	cin>>cases;
	
	for(int i=0;i<cases;i++){
		string winner="GABRIEL";
		int x,r,c;
		cin>>x>>r>>c;
		
		if(x>6){
			winner="RICHARD";
			
		}
		if((r*c)%x!=0){
			winner="RICHARD";
			
		}
		if(x>2){
			if( (c < (x/2)+1) || (r < (x/2)+1)){
				winner="RICHARD";
				
			}
		}
		cout<<"Case #"<<i+1<<": "<<winner<<"\n";
	}
	return 0;
}

