#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cmath>
#include<array>

using namespace std;

int main()
{
	int T,K,C,S,num;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>K>>C>>S;
		cout<<"Case #"<<t<<":";
		if((K<=S+1)&&C!=1)
		{
			if(K==1)
			{
				cout<<' '<<K;
			}
			else
			{
				while(K>1)
				{
					cout<<' '<<K;
					K--;
				}
			}
		}
		else if((C==1)&&(K<=S))
		{
			while(K>0)
			{
				cout<<' '<<K;
				K--;
			}
		}
		else
		{
			cout<<" IMPOSSIBLE";
		}
		cout<<endl;
	}
	return 0;
}
