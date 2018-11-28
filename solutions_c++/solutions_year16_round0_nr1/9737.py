#include<iostream>
using namespace std;
int main()
{
	int t,i,j,k,a,digit,number;
	int arr[10],digitno[10],digits[10];
	cin>>t;
	int *num = new int[t];
	int *num1 = new int[t];
	
	for(i=0;i<t;i++)
	{
		cin>>num[i];
		num1[i]=num[i];
	}
	
	for(i=0;i<t;i++)
	{
		
			for(k=0;k<10;k++)
	           {
	           	arr[k]=0;
               }
         a=0;
         
redo:   a=a+1;
        num[i]=a*num1[i];       
		digit=0;
		
		if(num[i]==0)
		{
		digit++;	
		}
		
	   number=num[i];
	   
	   while(number)
	   {
	    number=number/10;
		digit++; 	
	   }
	   
	   digitno[i]=digit;
	   number=num[i];
	   
	   for(j=0;j<digitno[i];j++)
	   {
   		digits[j]=number%10;
   		number=number/10;
   		arr[digits[j]]=1;
   	   }
   	   
   	   if(num[i]!=0)
   	   {
   	   	
   	       for(k=0;k<10;k++)
	           {
	           	
	           	if(arr[k]==0)
	           	{
	           		goto redo;
	           	}
	           	
	           	if(arr[k]==1 && k==9)
	           	{
	           		cout<<"Case #"<<i+1<<": "<<num[i];
	           		
	           		if((i+1)!=t)
	           		{
		           		cout<<"\n";
		           	}
	           		
	           	}
	           	
               }
   	   }
   	   else
   	      {
   	      	cout<<"Case #"<<i+1<<": INSOMNIA";
	           		
	           		if((i+1)!=t)
	           		{
		           		cout<<"\n";
		           	}
          }
   	   
	}
	
	
	
return 0;	
}
