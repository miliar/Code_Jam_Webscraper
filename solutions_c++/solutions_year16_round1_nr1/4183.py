#include <iostream>
using namespace std;

#include <string.h>

void insertAtStart(char *p, char j, int len)
{
	while(len--)
	{
		p[len+1] = p[len];

	}
	p[0] = j;
}

int main()
{
	int testCases;
	
	cin >> testCases;

	for(int i=1; i<=testCases;i++)
	{
		char res[1001];
		char str[1001];
		cin >> str;
		int strLength = strlen(str);
		res[0] = str[0];
		int resLenCounter=1;

		for(int j=1; j<strLength;j++)
		{
			if(str[j] >= res[0])
			{
				insertAtStart(res,str[j], resLenCounter);
				resLenCounter++;
			}
			else
			{
				res[resLenCounter++] = str[j];
			}

		}

		res[resLenCounter] = '\0';

		cout<<"Case #"<<i<<": "<<res<<endl;
	}// test case for

	return 0;
}

