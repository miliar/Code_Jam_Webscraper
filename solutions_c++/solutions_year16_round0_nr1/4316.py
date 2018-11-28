#include <iostream>
using namespace std;


int main ()
{
	int noofCase,count,mul;
	long long test,multi,multi2;
	cin>>noofCase;

	for(int i=1;i<=noofCase;i++)
	{
		cin>>test;
		int digit[]={0,0,0,0,0,0,0,0,0,0};
		if(test>0)
		{

			for(count =0 ,mul = 1;count<10;mul++)
			{
				multi2=multi = mul*test;
				while(multi2>0)
				{
					if(!(digit[multi2%10]))
					{
						digit[multi2%10]++;
						count++;
					}                                          
					multi2=multi2/10;
				}
			}
 
cout<<"Case #"<<i<<": "<<multi<<endl;
			}
else
	cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
 
         
	return 0;

}