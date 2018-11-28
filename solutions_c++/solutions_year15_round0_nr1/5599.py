#include <iostream>
#include <string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int j = 1;
	int k;
	while(j<=t)
	{
		cin>>k;
		string s;
		cin>>s;

		int friends = 0;
		int sum = 0; // number of persons currently standing
		for(int i=1;i<=k;i++)
		{
			sum += (s[i-1]-'0');
			if(sum >= i) // if number of people standing greater than the current shyness level
			{
				continue;
			}
			else
			{
				if((s[i] - '0') > 0)
				{
					friends += i-sum;
					sum += friends;
				}
			}

		}
		cout<<"Case #"<<j<<": "<<friends<<endl;
		j++;
		
		
	}
}