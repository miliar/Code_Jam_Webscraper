#include <iostream>
using namespace std;

int main()
{
  int noOfTestCases,n,m;
 
  cin>>noOfTestCases;
  for(int k=1; k<=noOfTestCases; k++)
  {
    cin>>n>>m;
     int a[n][m];
    	for(int i=0; i<n; i++)
  		{
          for(int j=0; j<m; j++)
  			{
          		cin>>a[i][j];
    
        	}
    
        }
    
    
    //logic
    string flag;
    int flag1,flag2;
	flag="YES";
   for(int i=0; i<n; i++)
  		{
          for(int j=0; j<m; j++)
  			{
            		flag1=1;
            		flag2=1;
          		if(a[i][j]==1)
                {
                  int ti=i;
                  int tj=j;
                  for(int j=0; j<m; j++)
  					{
          				if(a[ti][j]==2)
                          flag1=0;
                  	}
                  for(int i=0; i<n; i++)
  					{
          				if(a[i][tj]==2)
                          flag2=0;
                  	}
                  if( flag1==0 && flag2==0)
                    flag="NO";
                  i=ti;
                  j=tj;
    
                }	
    
                  
    
        	}
    
        }
   
    
    
    
    cout<<"Case #"<<k<<": "<<flag<<"\n";
    
  }//end of outermost for loop
  
  
  
  
  
   return 0;
}
   