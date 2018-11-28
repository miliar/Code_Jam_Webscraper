#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cassert>
using namespace std;

 int main() {
	
	int T;
   long long int N,temp;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
	    cin>>N;
		
	    if(N==0)
	    cout<<"case #"<<i<<": "<<"INSOMNIA"<<endl;
	    else
	    {
	        int array[10]={0},count=0,no,k;
	         no=N;k=1;
	        while(count!=10)
	        {
	            N=no*(k);temp=N;
	            while(N)
	            {
	                if(array[(N%10)]==0)
	                {
	                 count ++ ;
	                 array[(N%10)]=1;
	                 
	                }
	                N=N/10;
	            }
				k++;
	           
	        }
	        cout<<"case #"<<i<<": "<<temp<<endl;
	        
	    }
	}
	return 0;
}
