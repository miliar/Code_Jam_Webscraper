#include <iostream>
#include <string.h>
#pragma warning(disable:4996)
using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int t = 1; t <= T; t++)
	{
		char str[101];
		scanf("%s", &str);
		int L = strlen(str);

		int res = 0;
		
		for (int next = 1; next< L; next++)
		{
			char c = str[0];
			char n = str[next];

			if(c!=n)
			{
				res++;
				char what = str[next] == '+' ? '+' : '-';
				for (int i = 0; i < next; i++)
					str[i] = what;
			}
		}
		if(str[0] == '-')
			res++;

		cout<<"Case #"<<t<<": "<<res<<endl;
	}
	return 0;
}