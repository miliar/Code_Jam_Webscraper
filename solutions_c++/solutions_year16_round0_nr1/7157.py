#include<fstream>
#include<math.h>
#include<iostream>
#define type int
#define INPUTFILENAME "A-large.in"
#define OUTPUTFILENAME "largeOutputA.txt"
using namespace std;

int main(){
	bool digits[10];
	register unsigned short r,i,d,j,c;
    register type limit,t,n,m;
  	ifstream input;
  	ofstream output;
  	input.open (INPUTFILENAME);
  	output.open (OUTPUTFILENAME);
  	input>>c;
  	for(j=0;j<c;j++){
  		output<<"Case #"<<j+1<<": ";
    	input>>n;
  		if(n==0){
  			output<<"Insomnia\n";
  			continue;
	  	}
  		for(i=0;i<10;i++)
    		digits[i]=0;
  	
	  	i=d=m=0;
		t=m+=n;
  	
		//find #digits in t
		while(t){
			r=t%10;
			t=t/10;
			if(!digits[r]){
				digits[r]=1;
				i++;
			}
			d++;		
		}	
	
    	limit=(pow(10,d)-1)*10;	
    	while(i<10 && m<=limit){
        	t=m+=n;
        	//find #digits in m
			while(t){
				r=t%10;
				t=t/10;
				if(!digits[r]){
					digits[r]=1;
					i++;
				}		
			} 
   	
   		} 
   		if(i<10)
     		output<<"Insomnia\n";
   		else
     		output<<m<<"\n";
    
	}
  	input.close();
  	output.close();
  	return 0;
}
  
