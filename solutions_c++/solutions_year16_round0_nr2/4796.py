#include<iostream>
#include<list>
#include<algorithm>
#include<string>

using namespace std;

int main()
{
	int i, T;
	string stack[100];
	bool flip;
	
	cin>>T;
	for(int j = 0; j < T; j++)
		cin>>stack[j];
	
	for(int j = 0; j < T; j++)
	{
		long int countNum =0;
		
		while(true)
		{
		flip = false;	
		for(i=stack[j].length(); i > 0; i--)
		{	
			
			if((flip == false)&&(stack[j][i-1] == '-'))
				flip = true;
			if(flip == true)
				if(stack[j].front() == stack[j][i-1])
				{
					countNum++;
					break;
				}
					
			
		}
				
		reverse(stack[j].begin(), stack[j].begin() + i);
		for(int k = 0; k < i ; k++)
		{
			if(stack[j][k]=='-')
				stack[j][k] = '+';
			else
				stack[j][k] = '-';
				
		}
		
		
		if(count(stack[j].begin(), stack[j].end(), '+') == stack[j].length())
		 			break;
		}
		
		
		cout<<"Case #"<<j+1<<": "<<countNum<<endl;
	}
	
	return 0;
}
