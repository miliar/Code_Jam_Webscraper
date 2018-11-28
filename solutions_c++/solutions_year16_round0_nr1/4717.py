#include<iostream>
#include<algorithm>
#include<array>

using namespace std;

int main()
{
	int i = 1, temp;
	int T, N[100];
	long int curr, result;
	array<int, 10> digits; 
	
	cin>>T;
	for(int j = 0; j < T; j++)
		cin>>N[j];
	
	digits.fill(0);
	
	for(int j = 0; j < T; j++)
	{
	    curr = 0;
	    i=1;
	    digits.fill(0);
		while(true)
		{
		    if(N[j] == 0)
		        break;
			if(curr == 0)
			{
				
				curr = i*N[j];
				result = curr;
				i++;
			}
			
			while(curr != 0)
			{
			temp = curr%10;
			curr /= 10;
		 	
		 	if(digits[temp] == 0)
		 	{
		 		digits[temp] = 1;
		 		
			 }
			}
			if(count(digits.begin(), digits.end(), 1)==10)
		 			break;
					
		}
		
		if(N[j] == 0)
		cout<<"Case #"<<j+1<<": INSOMNIA"<<endl;
		else
		cout<<"Case #"<<j+1<<": "<<result<<endl;
	}
	
	return 0;
}
