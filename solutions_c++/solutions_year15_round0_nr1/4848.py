#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{

	freopen("A-large.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	int S;
	cin>>T;
	int c = 1;
	while (T--)
	{
		
		int count = 0;
		cin>>S;
		++S;
		char ch;
		int hasMember = 0;
		int step = 1;
		int required = 0;
		while (S--)
		{
			cin>>ch;
			int value = ch - '0';
			hasMember += value;

			if (hasMember < step)
			{
				required += step - hasMember;
				hasMember += step - hasMember;
			}
			++step;
		}
		cout<<"Case #"<<c++<<": "<<required<<endl;
	}
	return 0;
}