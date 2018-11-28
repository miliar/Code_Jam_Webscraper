#include <fstream>
#include <iostream>
#include <string.h>

using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */


char mul(char x,char y,int & sign)
{
  if (x=='0')
  {
  return y;                   
  }  
  else if (x=='1')  
  {          
  return y;                             
  }  
  else if (x=='i')  
  {
  if (y=='1') return 'i';
  else if (y=='i') {sign=-sign; return '1'; } 
  else if (y=='j') { return 'k';} 
  else if (y=='k') {sign=-sign; return 'j';}                              
  }
            
  else if (x=='j')  
  {        
    if (y=='1') return 'j';
  else if (y=='i') {sign=-sign; return 'k';} 
  else if (y=='j') {sign=-sign; return '1'; }
  else if (y=='k') { return 'i'; }                  
  }  
  else if (x=='k')  
  {
   if (y=='1') return 'k';
  else if (y=='i') { return 'j';} 
  else if (y=='j') {sign=-sign; return 'i'; }
  else if (y=='k') {sign=-sign; return '1'; }              
        
  }                          
     
     
}     



int main(int argc, char** argv) 
{	
	ifstream in("C-small-attempt0.in");
	ofstream out("C-small-attempt0.out");
	int sign = 1;
	long long int testcases;
	in >> testcases;
	
	//loop on test cases
 	for (int i = 1 ; i<= testcases; i++)
	{
		sign = 1;
		long long int L,X, count = 0; //count is 1 when found i ,, ,, 2 if found i & j  ,, ,, 3 if found i,j,k
		
		in >> L >> X;
		long long int mm = X;  // L is array length ,,,,, x is occurances
		char str[100000];
		in >> str;
		for(int j = 1; j < X; j++ )
		{
		    strncat(str,str , L);
        }
        X = mm;
		if (strlen(str) < 3) 
		{
		    out<<"Case #"<<i<<": "<< "NO"<<endl;
	    	continue;
		}
		int m = 0;
		if (str[0] == 'i') 
		{
		    count++;
		    m = 1;
		    if(str[1] =='j')
		    {
		    	count++;
		    	m=2;
		    	if(str[2]=='k')
		    	{
		    		out<<"Case #"<<i<<": "<<"YES"<<endl;
		    		continue;
		    	}
		    }
	    }

        char current_result = mul(str[m] , str[m+1], sign);
		if (((m==0)&&(current_result == 'i')&&sign) || ((m==1)&&(current_result == 'j')&&sign) || ((m==2)&&(current_result == 'k')&&sign))
		{
		count++;
		current_result = '0';
	    }
		m+=2;
		
		if ( count == 0)
		{
			//check for i  till you find it
			for (int q = m; q < L*X; q++)
			{
				current_result = mul(current_result , str[q] , sign);
				if (current_result == 'i' && sign==1)
				{
					count++;
					current_result = '0';
					m = q+1;
					break;
				}
			}
		}
	
		if ( count == 1)
		{
			//check for j till you find it
		    for (int q = m; q < L*X; q++)
			{
				current_result = mul(current_result , str[q] , sign);
				if (current_result == 'j'  && sign==1)
				{
					count++;
					current_result = '0';
					m = q+1;
					break;
				}
			}
		
		}
	
		if ( count == 2)
		{
			//check for k till the end of array
		for (int q = m; q < L*X; q++)
			{
				current_result = mul(current_result , str[q] , sign);
			}
		if (current_result == 'k'  && sign==1)
			{
				count++;
			}
        }     
	
	if(count == 3) out<<"Case #"<<i<<": "<<"YES" <<endl;
	else out<<"Case #"<<i<<": "<< "NO" << endl;
	count = 0;
	} 

	return 0;
}
