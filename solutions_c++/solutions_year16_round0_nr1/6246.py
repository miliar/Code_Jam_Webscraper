#include <iostream>
#include <string.h>

using namespace std;

bool isUsed[10];

int main()
{
	int T;
	cin>>T;
	for (int t = 1; t <= T; t++)
	{
		int N;
		cin>>N;
		if(N==0){
			cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
			continue;
		}

		memset(isUsed, false, sizeof isUsed);
		
		int res = 1;
		while(true)
		{
			int tmp = N*res;
			while(tmp>0)
			{
				int here = tmp%10;
				isUsed[here] = true;
				tmp/=10;
			}

			bool flag = true;
			for (int i = 0; i < 10; i++)
			{
				if(!isUsed[i])
				{
					flag=false;
					break;
				}
			}

			if(flag)
				break;
			res++;
		}
		
		cout<<"Case #"<<t<<": "<<N*res<<endl;
	}
	return 0;
}