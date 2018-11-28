#include <iostream>
#include <fstream>
using namespace std ;

ifstream in ("input.txt");
ofstream out ("output.txt") ;

int t,x,r,c ;
main(){
	in>>t ;int n = 0 ;
	while(t--){
		n++;
		in>>x>>r>>c ;
		if((r*c)%x != 0){
			out<<"Case #"<<n<<": RICHARD"<<endl;
		}
		else{
			if((r*c)/x >= x-1){
				out<<"Case #"<<n<<": GABRIEL"<<endl;
			}
			else{
				out<<"Case #"<<n<<": RICHARD"<<endl;
			}
		}
	}
}
