#include<fstream>
#include<math.h>
#include<string>
#define INPUTFILENAME "B-large.in"
#define OUTPUTFILENAME "smallOutputB.txt"
using namespace std;

int main(){
	
	register unsigned short i,t;    
	register char c1, c2;
	register int flip;
	string s;
	ifstream input;
  	ofstream output;
  	input.open (INPUTFILENAME);
  	output.open (OUTPUTFILENAME);
  	input>>t;
  	input.get(c1);
  	for(i=0;i<t;i++){
  		output<<"Case #"<<i+1<<": ";
  		flip=0;
    	getline(input,s);
    	int i=0;
		if(s[i]!='\0'){
	    	if(s[i+1]!='\0'){
    			while(true){
					if(s[i+1]=='\0'){
		    			break;
	    			}
					else if(s[i]!=s[i+1]){
							++flip;			
					}
					++i;
				}
			}
			if(s[i]=='-')
		  		++flip;
		}
		output<<flip<<"\n";
	}
	  		
  	input.close();
  	output.close();
  	return 0;
}
  
