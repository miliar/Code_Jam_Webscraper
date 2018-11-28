#include <iostream>  
#include <cmath>
#include <string> 
using namespace std;

int main ()
{
	int t,count;
	long long n,m;
	cin>>t;
	for(int i = 1; i <= t; i++)
	{
		count = 0;
		bool a[10] = {0};
		cin>>n;
		m = n;
		if(n == 0)
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		else
		{
			while(true)
			{
				string s = to_string(n);
				for(int i = 0; i < s.length(); i++)
				{
					if(a[s[i] - 48] == 0)
					{
						a[s[i] - 48] = 1;
						count ++;
					}
				}
				if(count == 10)
				{
					cout<<"Case #"<<i<<": "<<n<<endl;
					break;
				}
				n += m;
			}
		}
	}
  return 0;
}