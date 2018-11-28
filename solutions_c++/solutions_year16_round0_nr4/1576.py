#include<iostream>
#include<string>
#include<string.h>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("Output4-1.txt","w",stdout);
	int T,K,C,S;
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		cin>>K>>C>>S;
		int p=K / 2;
		int Rem=K % 2;
		cout<<"Case #"<<i<<": ";
		//if(S*C<K) cout<<"IMPOSSIBLE"<<endl;
		//else
		{
			for(int j=1; j<=K; j++)
			{
				cout<<j<<" ";
			}
			cout<<endl;
		}
	}
	return 0;
}
