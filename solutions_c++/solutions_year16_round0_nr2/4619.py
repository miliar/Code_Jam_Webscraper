#include <iostream>
#include <cstring>
using namespace std;

int main(int argc, char const *argv[])
{
	int t,m=1,steps,i,len;
	char str[200],a;
	cin>>t;
	while(m<=t)
	{
		cin>>str;
		steps = 0;
		len = strlen(str);
		i = 1;
		while(i < len)
		{
			if(str[i-1] != str[i])
			{
				for(int j = 0; j<i; ++j)
				{
					if(str[j] == '+') str[j] = '-';
					else str[j] = '+';
				}
				i = 1;
				steps++;
			}
			else
				++i;
		}
		if(str[0] == '-')
			steps++;
		cout<<"Case #"<<m<<": "<<steps<<endl;
		m++;
	}
	return 0;
}