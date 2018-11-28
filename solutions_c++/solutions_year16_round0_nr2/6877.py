#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<map>
#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<map>
#include<vector>
#include<list>
#include<queue>
#include<algorithm>
#include<limits>
#include<time.h>
using namespace std;

int main()
{
	int T;
	string s[101];
	cin>>T;
	for(int i=0;i<T;i++)
		cin>>s[i];
	for(int i=0;i<T;i++)
	{
		int cnt = 0;
		for(int j=s[i].size()-1;j>=0;j--)
		{
			if(s[i][j] == '-')
			{
				cnt++;
				for(int k=0;k<=j;k++)
					s[i][k] == '+'?s[i][k] = '-':s[i][k] = '+';
			}
		}
		cout<<"Case #"<<i+1<<": "<<cnt<<"\n";
	}
	return 0;
}