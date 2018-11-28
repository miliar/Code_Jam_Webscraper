#include <iostream>
#include <fstream>
using namespace std ;

ifstream in ("input.txt");
ofstream out ("output.txt") ;

int p ,x,n = 0 ;
char c ;
main(){
	in>>p;
	while(p--){
		n++;
		int pplstd = 0 , ans = 0;
		in>>x;
		int array[x+1];
		for(int i = 0 ; i<=x ; i++){
			in>>c;
			array[i] = c-48;
			if(array[0] == 0 && i == 0){
				ans++;
				pplstd++;
			} 
			if(pplstd < i){
				ans += (i-pplstd) ;
				pplstd += (i-pplstd);
			}
			pplstd += array[i];
		}
		out<<"Case #"<<n<<": "<<ans<<endl;
	}
}
