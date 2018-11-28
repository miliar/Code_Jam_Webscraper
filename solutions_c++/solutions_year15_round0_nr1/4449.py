#include <iostream>

using namespace std;

int main()
{
	unsigned int t,s;
	string ppl;
	cin >> t;
	for(unsigned int i=0;i<t;i++)
	{
		unsigned int current=0,needed=0;
		cin >> s >> ppl;
		for(unsigned int j=0;j<ppl.length();j++)
		{
			if(current < j)
			{
				current++;
				needed++;
			}
			current += ppl[j] - '0';
		}
		printf("Case #%u: %u\n",i+1,needed);
	}
}