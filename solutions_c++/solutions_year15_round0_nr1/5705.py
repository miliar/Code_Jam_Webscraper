#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main (void)
{
	int T;
	cin>>T;
	for(int ti=1; ti<=T; ti++)
	{
		int max;
		cin >> max;
		char* numbers = new char[max+1];
		//scanf("%s",numbers);
		cin >> numbers;
		//cout<<"Case "<<ti<<","<<max<<","<<numbers<<endl;

		int need = 0;
		int cur = numbers[0] - '0';
		int count = 0;

		for(int i=1; i<=max; i++)
		{
		//	cout<<cur<<","<<need<<endl;
			count = numbers[i]-'0';
			if(cur>=i)
			{
				cur += count;
			}
			else
			{
				need += i - cur;
				cur += i - cur + count;
			}
		}
		cout<<"Case #"<<ti<<": "<<need<<endl;
	}
	return 0;
}
