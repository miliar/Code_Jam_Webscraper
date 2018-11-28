#include<fstream>
#include <iostream>
#include <stdlib.h>
using namespace std;
int temp[10];
int helper=0;


int caldigits(int num2,int temp[])
{
	while(num2>0)
	{
		int num3=num2%10;
		//cout<<"\t"<<num3<<"\t";
		num2=num2/10;
		temp[num3]=num3;helper++;
		
	}
	
	//cout<<endl;
	return 0;
}
int cal(int num)
{
	
	
	int i=1,num2,sum1;
	while(sum1!=45)
	{	
		num2=num*i;
		i++;
		int n=caldigits(num2,temp);
		int sum=0;
		for(int o=0;o<10;o++)
		{
			sum=sum+temp[o];
			
	//		cout<<"sum="<<sum<<"temp["<<o<<"]="<<temp[o]<<endl;
				
		}
		sum1=sum;
	}
	
	return num2;//return num;
}


int main()
{
  int textcno; 
  int arr[1000000],m,n;
  ifstream File;
    		File.open("A-large.in");
		File >> n;
		while(m<100)
    		{
       			 File >> arr[m];
        		 m++;
    		}
		
    		File.close();
   	  
	  //for(int i = 0; i < argc-2; i++) 
          //cout<<arr[i];
	  for(int i=0;i<n;i++)	
	  {
		if(arr[i]==0)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}		
		
		else
		{
			for(int o=0;o<10;o++)
			{
				temp[o]=11;
			}
			int n=cal(arr[i]);
			cout<<"Case #"<<i+1<<": "<<n<<endl;
			
		}	
		
	  }
	  	
  
  return 0;
}




