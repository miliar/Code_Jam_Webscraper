#include <iostream>
using namespace std;

int main() {
   int t,a[10],i,j,k,n,d,count,num;
   cin>>t;
   
  for(k=1;k<=t;k++)
   { 
    for(j=0;j<10;j++)
   a[j]=0;
      cin>>n;
      i=0;
      if(n==0)
      cout<<"case #"<<k<<": INSOMNIA"<<endl;
      else
      {   count=0;
      while(count<10)
    {  i++; 
	   num=i*n;
        
         while(num>0)
         {
            d=num%10;
            if(a[d]!=1)
            {
            	a[d]=1;
            	count++;
			}
           num=num/10;
         }
         
      }
      cout<<"case #"<<k<<": "<<i*n<<endl;
      }
      
   }
	return 0;
}
