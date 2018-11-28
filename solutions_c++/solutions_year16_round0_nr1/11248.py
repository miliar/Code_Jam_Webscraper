#include <iostream>
#include <cstdio>
#include <cstring>
#define IO ios_base::sync_with_stdio(0); cin.tie(0);
#define endl '\n'
using namespace std;

bool digit[15];

int main()
{
	IO
	int test;
	cin>>test;
	int cont = 1;
	while(test)
	{
		memset(digit, 0, sizeof(digit));
		int num;
		cin>>num;
		
		if(num == 0)
			cout<<"Case #"<<cont<<": INSOMNIA"<<endl;
		else
		{
			for(int i = 1; i <= 1000; ++i)
			{
				int temp = num*i;
				
				while(temp)
				{
					digit[temp%10] = true;
					temp /= 10;
				}
				bool fl = true;
				for(int j = 0; j < 10; ++j)
					if(!digit[j])
					{
						fl = false;
						break;
					}
				if(fl)
				{
					cout<<"Case #"<<cont<<": "<<num*i<<endl;
					break;
				}
				
			}
		
		
		}
		
		++cont;
		--test;
	}
	
	
	return 0;
}