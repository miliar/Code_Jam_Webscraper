#include <iostream>
#include <fstream>
#include <cmath>
#include <iostream>
#include <string.h>
using namespace std;

int t, s=1;
int a, b, n, p, c, i, l, m;
float r;
bool palin;
int main(void){
	ifstream in("C-small-attempt0.in") ;
	ofstream out("c.out") ;

	in >> t ;
	while(s<=t){
		char num[1000];
		out << "Case #" << s << ": " ;
		c=0;
		in >> a >> b;
		for(n=a ; n<=b ; n++){
			palin = true;
			r=sqrt(n);
			if(ceil(r)==floor(r)){
				 m = ceil(r);
				 sprintf(num,"%d",n); 
				 l = strlen(num);
				 for(i=0; i<l/2; i++){
						if(num[i] != num[l-1-i])
							palin=false;
							} 
				if(palin){
						sprintf(num,"%d",m);
						l = strlen(num);
						for(i=0; i<l/2; i++){
							if(num[i] != num[l-1-i])
								palin=false;
								}
							if(palin)
								c++;
							}
						}
			}	
		out  << c << endl ; 
		s++;
		}
	return 0;
	}
