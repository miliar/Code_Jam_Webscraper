#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

typedef long long int LL;
typedef unsigned long long int ULL;

int main()
{
	int t, smax, tc=0;
	
	cin>>t;
	
	while(t--)
	{
		++tc;

		cin>>smax;
		
		string str;
		int mini = 0, total=0;
		
		cin>>str;
		
		total = str[0]-'0';
		
		//cout<<"Inititally total : "<<total<<endl;
		
		for(int i=1;i<=smax;i++)
		{
			if(total < i)
			{
				//cout<<"Not enough : "<<total<<" < "<<i<<"         ";
				
				mini += (i-total);
				total += (i-total);
				
				//cout<<"Mini : "<<mini<<" and total : "<<total<<endl;
			}
			
			total += str[i]-'0';
			
			//cout<<"Final total after "<<i<<" = "<<total<<endl;
		}
		
		cout<<"Case #"<<tc<<": "<<mini<<endl;
	}
	return 0;
}
