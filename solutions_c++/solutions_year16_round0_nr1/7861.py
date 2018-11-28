#include <iostream>




using namespace std;

int main (void)
{
	int test;
	cin>>test;

	for(int j=1;j<=test;j++)
	{
		bool number_occured[10]={0};
		int count=0;
		int number=10;
		cin>>number;
		int init=number;
		if (number==0)
		{
			cout<<"Case #"<<j<<": INSOMNIA"<<endl;
		}
		else
		{



			int i=0;
			
			while(count<10)
			{
				// break the number into component;
				number=init*(i+1);
				int temp=number;
				//cout<<"count"<<count<<endl;
				//cout<<"number : "<<number<<endl;

				while(temp>0)
				{
					//cout<<"temp:"<<temp<<endl;
					int _remainder=temp%10;
					//cout<<"iteration"<<i;
					//cout<<"_remainder"<<_remainder<<endl;
					temp=temp/10;
					if(number_occured[_remainder]==0)
					{
						number_occured[_remainder]=1;
						count++;
					}

				}

				i++;
				
				

			}
			cout<<"Case #"<<j<<": "<<number<<endl;
		}


	}

	
	

	return 0;
}