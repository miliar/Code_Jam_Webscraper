#include<iostream>
#include<string>


using namespace std;

int main()
{
	char flag = 1;
	int testCases, Smax,s,caseCount,sum, y;
	string seats;

	ios::sync_with_stdio(false);

	cin>>testCases;
	for(caseCount = 1; caseCount <= testCases; caseCount++)
	{
		cin>>Smax>>seats;
		sum = y = 0;

		for(s=0 ; s<=Smax; s++)
		{
			sum += seats[s] - '0';
			
			for(flag = 0;seats[s]=='0'; s++,flag =1);
			
			if(s>sum)
			{
				y += s-sum;
				sum += s-sum;
			}
			
			if(flag)
			{
				sum += seats[s] - '0';
			}
			

		}
		
		cout<<"Case #"<<caseCount<<": "<<y<<endl;
	}

	return 0;
}

