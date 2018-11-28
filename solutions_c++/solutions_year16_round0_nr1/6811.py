
#include <iostream>
#include <fstream>
#define toDigit(c) (c-'0')
using namespace std;

int main () {
	int count;
  	int result, n, l, d;
  	
	ifstream input;
	ofstream output;
  	
	//input.open("A-sample.in", std::ios_base::in);
  	//output.open("A-sample.out", std::ios_base::out);
	
  	//input.open("A-small.in", std::ios_base::in);
  	//output.open("A-small.out", std::ios_base::out);
  	
	input.open("A-large.in", std::ios_base::in);
  	output.open("A-large.out", std::ios_base::out);
	    	
  	input >> count;

  	for(int i=1; i<=count; i++)
  	{
  		input>>n;

  		l = 1;
  		
  		bool iar1[10] = {0,0,0,0,0,0,0,0,0,0};
  		bool iar2[10] = {1,1,1,1,1,1,1,1,1,1};
  		
  		if(n == 0)
  		{
  			output<<"Case #"<<i<<": INSOMNIA"<<endl;
	  	}
	  	else
	  	{
	  		while(1)
	  		{
	  			result = d = n * l;

	  			do 
				{
				    int digit = d % 10;
				    iar1[digit] = 1;
				    d /= 10;
				} while (d > 0);
	  			
	  			bool flag = true;
	  			for(int x=0; x<10; x++)
	  			{
	  				if(iar1[x] != iar2[x]) flag = false;	
				}
				
				if(flag == true) break;
				
				l++;
			}
	  		
	  		output<<"Case #"<<i<<": "<<result<<endl;
	  	}
  		
	}  	
  
  	input.close();
  	output.close();
  	
  	return 0;
}
