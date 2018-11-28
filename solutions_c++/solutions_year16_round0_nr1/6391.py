#include <iostream>
#include<fstream>
using namespace std;

long int arr[]={0,1,2,3,4,5,6,7,8,9};


int main()
{
	ifstream fi;
	fi.open("A-large.in",ios::in);
	
	ofstream fo;
	fo.open("A-large.out",ios::out);
	
	long int test,k,temp,last,count=0,rem,visited[10],num,num2,size=0;
	
	fi>>test;

	
	
	for(int i=0;i<test;i++)
	{    	
		fi>>num;
		count=0;
	
		if(num==0)
		{
		   fo<<"Case #"<<i+1<<":"<<" "<<"INSOMNIA"<<"\n";
		   continue;
	     }
		 temp=num;
		for(int j=0;j<10;j++)
		 {  visited[j]=j;}
		   k=2;
	  while(count<10)
	  {
	  	 
	  	 last=temp;
	  	
		while(temp!=0)
		{
		
			rem=temp%10;
			if(visited[rem]==rem)
			{  
			   visited[rem]=999;
			   count=count+1;
			   
		    }
		    
		    temp=temp/10;
		    
		}
		
		temp=num*k;
		
		
		k++;
	  }
	
      
    

	fo<<"Case #"<<i+1<<":"<<" "<<last<<"\n";
	
   }
   fi.close();
   fo.close();
   return 0;
} 
		    
		    
		    
		       
				
