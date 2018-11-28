#include <iostream>
using namespace std;


int main()
{
	long arr[10],test,num,i,count,j,temp,rem,output,cse=1;
	cin>>test;
	while( test-- )
	{
		cin>>num;
		count = 0;
		j = 1;
		for( i = 0 ; i < 10 ; i++ )
			arr[i] = 0;
		if( num == 0 )
		{
			cout<<"Case #"<<cse<<": "<<"INSOMNIA"<<endl;
			cse++;
			continue;
		}
		while( count != 10 )
		{
			output = temp = num * j;
			while(temp)
			{
				rem = temp % 10;
				if( arr[rem] == 0 )
				{
					count++;
					arr[rem] = 1;
				}
				temp = temp / 10;
			}
			j++;
		}
		cout<<"Case #"<<cse<<": "<<output<<endl;
		cse++;

	}
	return 0;
}

