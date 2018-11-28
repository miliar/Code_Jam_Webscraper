#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <unordered_map>
#include <list>
using namespace std;


int main()
{
	freopen("input1.in", "r", stdin);
	freopen("output1.txt","w",stdout);
	ios_base::sync_with_stdio(0);

	int test;
	cin>>test;


	for(int t=1;t<=test;t++)
	{
		string s;
		cin>>s;

		list<char> arr;

		arr.push_back(s[0]);
		for(int i=1;i<s.length();i++)
		{
			if(int(s[i]) >= arr.front() )
			{
				arr.push_front(s[i]);
			}
			else
			{
				arr.push_back(s[i]);
			}
		}
		

		list<char>::iterator i;
		printf("Case #%d: ",t);
		for(i=arr.begin();i!=arr.end();i++)
		{
			printf("%c",*i);
		}
		printf("\n");

	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
