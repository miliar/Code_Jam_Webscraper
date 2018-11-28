#include <iostream>

using namespace std;

void make (int t, long long a)
{
	if (a==0)
		cout<<"Case #"<<t<<": INSOMNIA\n";
	else
	{
		bool je[12];
		int counter=0;
		int rounds=1;
		for(int i=0;i<10;i++)
		{
			je[i]=false;
		}
		long long last;
		while(counter<10)
		{
			long long b=a*rounds;
			rounds++;
			while(b>0)
			{
				int c=b%10;
				b/=10;
				if (je[c]==false)
				{
					counter++;
					je[c]=true;
				}
			}
			last=a*(rounds-1);
		}
		cout<<"Case #"<<t<<": "<<last<<endl;
	}
}

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		long long a;
		cin>>a;
		make(i+1,a);
	}
	return 0;
}
			
