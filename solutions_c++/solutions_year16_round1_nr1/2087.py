#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int t;
string input,temp;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		cin>>input;
		temp=input[0];
		for(int j=1;j<input.length();j++)
		{
			if(input[j]>=temp[0])
			{
				temp=input[j]+temp;
				//cout<<temp<<endl;
			}
			else
			temp+=input[j];
		}
		cout<<"Case #"<<i<<": "<<temp<<endl;
	}
}
