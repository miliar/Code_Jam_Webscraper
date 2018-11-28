#include <iostream>
#include<math.h>
#include<string.h>
#include<cstdlib>
using namespace std;
long long int isPrime(long long int n){
   long long  int i;

    if (n==2)
        return 1;

    if (n%2==0)
        return 2;

    for (i=3;i<=sqrt(n);i+=2)
        if (n%i==0)
            return i;

    return 1;
}


int main() {
	// your code goes here
	char s[17];
	long long int cal[17],is[17];
	int t,i,a,j,temp=0,count=0,m,n;
	cin>>t;
	cin>>m>>n;
	cout<<"Case #1:"<<endl;
	while(count!=50)
	{   s[0]=49;
	    s[15]=49; 
	    for(i=1;i<15;i++)
	     {
	           
	              s[i]=(rand()%2)+48;
	              //cout<<s[i]<<" ";
	             
	         
	     }
	     s[15]=49;
	     //s[14]=49;
	     
	    //a=strlen(s);
	    //cout<<a<<endl;
	   for(j=2;j<=10;j++)
	     {   cal[j]=0;
	         temp=0;
	        for(i=15;i>=0;i--)
	         {
	             cal[j]+=(s[i]-48)*pow(j,temp);
	              //cout<<cal[j]<<" ";
	               temp++;
	         }
	        // cout<<cal[j]<<" "<<isPrime(cal[j]);
	         //cout<<endl;
	        is[j]=isPrime(cal[j]); 
	     }
	     int f=0;
	     for(j=2;j<=10;j++)
	       {
	           if(is[j]==1)
	            {  f=1;
	                break;
	            }
	       }
	    if(f==0)
	    {  for(i=0;i<16;i++)
	       cout<<s[i];
	       cout<<"  ";
	        for(j=2;j<=10;j++)
	          cout<<is[j]<<" ";
	         count++; 
	        cout<<endl; 
	    }
	    
	    
	}
	
	return 0;
}
