#include <iostream>
#include <vector>
using namespace std;

vector<int> vec;

bool in_vector(int n )
{
	bool flag=false;
	int i;

	for(i=0;i<vec.size();i++)
		if(vec[i]==n)
		{
			// cout<<vec[i]<<" here "<<n<<'\n';
			flag=true;
			break;
		}

	// cout<<"Passed : "<<n<<" returned : "<<flag<<'\n';	

	return flag;	
}

void split(long long int num)
{
	int r;
	long long int x= num;

	while(x>0)
	{
		r=x%10;

		r=(r==0)?10:r;

		if(!in_vector(r))
		{
			// cout<<"pushed "<<r<<'\n';
			vec.push_back(r);
		}
		// cout<<x<<'\n';

		x/=10;

	}
}

int main()
{
	int t , i;
	cin>>t;

	for(i=0;i<t;i++)
	{
		long long int n , k;
		cin>>n;
		bool done=false;

		for(k=1;done==false;k++)
		{
			if(n!=0)
			{
				long long int current=k*n;
				split(current);
				// cout<<vec.size()<<'\n';
				if(vec.size()>=10)
				{
					done=true;
					vec.clear();
					cout<<"Case #"<<i+1<<": "<<current<<'\n';
				}
			}
			else
			{
				done=true;
				vec.clear();
				cout<<"Case #"<<i+1<<": INSOMNIA"<<'\n';
			}	

		}
	}



	return 0;
}