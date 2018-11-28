#include<iostream>
#include<string.h>
using namespace std;
int main()
{
//Input number of cases.
int number,min_step,a,j;
cin>>number;
//For that many cases...
for(int i=0;i<number;i++)
{
	//Display Case number,  and initializing stuff...
	cout<<"Case #"<<i+1<<": ";
	char list[110];
	min_step = 0;
	cin>>list; 					//Accept List of Pancakes(+ and -)
	int len = strlen(list);				//Calculate list length
	while(true)
	{
		{					//Condition to quit loop
		for(j=0;j<len;j++)
			if(list[j] == '-')
				break;
		if(j == len)
			break;
		}
		if(list[0] == '+')			//Set first elements to - if it is +(Cause flipping reverses the order.
			{
				for(j = 0;j < len;j++)
				{
					if(list[j] == '+'){list[j] = '-';}
					else{break;}
				}
				min_step++;
			}


		for(j=len-1;j>=0;j--)			//Find location of last - sign.
			if(list[j] == '-')
				{break;}


		if(j > -1)
		{					//If no - found, do nothing.


		if((j+1)%2==0)				//Case 1 : Even number of pancakes to flip
		{
		for(a=j;a>=(j+1)/2;a--)
		{
			char temp;
			temp = list[j-a];
			if(list[a] == '-'){list[j-a] = '+';}
			else{list[j-a] = '-';}
			if(temp == '-'){list[a] = '+';}
			else{list[a] = '-';}

		}
		}
		else					//Case 2 : Odd number of pancakes to flip.
		{
		for(a=j;a>=(j+2)/2;a--)
		{
			char temp;
			temp = list[j-a];
			if(list[a] == '-'){list[j-a] = '+';}
			else{list[j-a] = '-';}
			if(temp == '-'){list[a] = '+';}
			else{list[a] = '-';}


		}
			if(list[j/2]=='+'){list[j/2]='-';}
			else{list[j/2]='+';}
		}

		min_step++;				//Increment Min. Steps
		}
	}
	cout<<min_step<<endl;
}
return 0;
}
