#include<algorithm>
#include<stack>
#include<queue>
#include<string>
#include<vector>
#include<string.h>
#include<iostream>
#include<fstream>
#include<ctype.h>
#include<math.h>
#include<memory>
#include<climits>
using namespace std;
int main()
{
	
	ifstream fi("B-large.in",ios::in);
	ofstream fo("B-large.out",ios::out);
	int test;
	fi>>test;
	
	for(int i=0;i<test;i++)
	{  
	   int N,matrix[200000],count=1,d=0;
		fi>>N;
		int s=0,a[200000];
		for(int k=0;k<(2*N-1);k++)
			  {
			  		for(int j=0;j<N;j++)
		          {
		
			  	      fi>>matrix[s];
						s++;
			  	  }
			  }
			  
			  
			 sort(matrix,matrix+s);
			 for(int m=1;m<=s;m++)
			 {
			 	if(matrix[m]==matrix[m-1])
			 	  {
				   count++;
			     }
			     else 
			     {
			     	if((count%2)!=0)
			     	  { 
					   a[d]=matrix[m-1];
			     	   d++;
			           }
			     	   count=1;
			     }
			 }
			 
			 
			 sort(a,a+d);
			 
			 fo<<"Case #"<<i+1<<":"<<" ";
			 for(int m=0;m<d;m++)
			 {
			 	fo<<a[m]<<" ";
			 }
			 fo<<"\n";
			 memset(a,0,sizeof(a));
			 
			 
		}
		
		return 0;
			 	  
			  
			  
		
			  	      
			  	          
			  	        
			  	             
			  	        
			  	 
			  
	
}


