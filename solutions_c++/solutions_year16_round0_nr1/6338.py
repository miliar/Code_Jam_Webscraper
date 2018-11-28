#include <iostream>
#include <fstream>
#include<cstdio>
using namespace std;

int main() {
	// your code goes here
	ifstream in;
	ofstream of;
	in.open("input.txt");
	of.open("output.txt");
	int t,i;
	in>>t;
   for(i=0;i<t;i++)
	{
     int n,k,j;
      k=1;
	in>>n;
      int a[10];
      int count=10;
      for(j=0;j<10;j++)
        a[j]=0;
    if(n==0)
//printf("Case #%d: INSOMNIA\n",i+1,n*k);
	of<<"Case #"<<(i+1)<<": "<<"INSOMNIA"<<"\n";
	else
	{
	    while(count!=0)
	    {
	        
	        int x=k*n;
	        while(x>0)
	        {
	            if(a[(x%10)]==0)
	             {
	                 count--;
	                 a[(x%10)]=1;
	             }
	             x=x/10;
	             
	        }
	        if(count==0)
	        break;
	        k++;
	        
	    }
       //  printf("Case #%d: %d\n",i+1,n*k);
	   of<<"Case #"<<(i+1)<<": "<<(k*n)<<"\n"; 
	    
	}
	}
	return 0;
}

