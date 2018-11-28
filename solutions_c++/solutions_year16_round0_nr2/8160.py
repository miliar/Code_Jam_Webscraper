#include<iostream>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output7.in","w",stdout);

	int t;
	cin>>t;
	
	int k = t;
	
	while(t--)
	{
		char str[102];
		cin>>str;
		
		int length = 0;
		
		for(int i=0; str[i]!='\0';i++)
		{
			length ++;
		}
		
		str[length++] = '+';
		
		str[length] = '\0';
		
		char prev = '0';
		int skip = 0;
		
		int count = 0;
		
		
		for(int i=0;str[i]!='\0';i++)
		{
			if(str[i]== '-' && prev == '+')
			{
				int temp = 0;
				for(int j = i; str[j] == '-';j++)
				{
					temp++;
				}
				count = count + 2;
				prev = '+';
				i= i+temp-1;	
					
			}
			else if(str[i]=='+' && prev == '-')
			{
				count = count + 1;
				prev = '+';
			}
			else
			{
				prev = str[i];				
			}
//			cout<<"Count is "<<count<<endl;
		}
		
		
		cout<<"CASE #"<<k-t<<": "<<count<<"\n";
	}
}
