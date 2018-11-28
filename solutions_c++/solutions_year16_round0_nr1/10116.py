#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int T;
	unsigned long int N;
	cin>>T;

	for(int i=0; i<T; i++)
	{
		int array[10];
		for(int j=0; j<10; j++)
			array[j] = 1;

		cin>>N;
		if(N == 0)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA\n";
		}
		else
		{	
			unsigned long int counter = 0;
			counter = 0;
			int test = 1;
			while(test!=0)
			{
				counter++;
				int N_val = counter*N;

				while(N_val>0)
				{
					array[N_val%10] = 0;
					N_val = N_val/10;
				}

				test = 0;
				int x = 0;
				for(x=0; x<10; x++)
				{
					test += array[x];

				}
							
			}
			cout<<"Case #"<<i+1<<": "<<counter*N<<"\n";	
		}

	}

}