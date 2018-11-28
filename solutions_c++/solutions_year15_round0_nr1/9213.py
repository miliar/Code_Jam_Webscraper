#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int main()
{
	freopen("A-large.in","rt",stdin);
	int tests = 0;
	int s_max = 0;
	cin>>tests;
	
	for(int i = 0;i<tests;i++)
	{
		int standing_count = 0;
		int to_add = 0,final_add = 0;
		cin>>s_max;
		char ip[s_max+1];
		int num_ip[s_max+1];
		
		for(int j = 0;j<=s_max;j++)
		{
			cin>>ip[j];
			num_ip[j] = int(ip[j] - '0');
		}
		
		standing_count = num_ip[0];
		
		for(int j = 1; j<=s_max; j++)
		{
			if(standing_count < j)
			{
				to_add = to_add + j - standing_count;
				standing_count += num_ip[j] + to_add;
				final_add += to_add; 
				to_add = 0;
			}
			
			else 
			{
				standing_count += num_ip[j];
			}
		}
		
		freopen("A-smalllsl.out","a+",stdout);
		cout<<endl<<"Case #"<<i+1<<": "<<final_add;
		fclose(stdout);
		/* Printing the array
		for(int j = 0; j <= s_max; j++)
			cout<<num_ip[j];
		*/
	}
	
	
	return 0;
}
