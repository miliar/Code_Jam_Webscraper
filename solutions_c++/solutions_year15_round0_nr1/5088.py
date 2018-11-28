#include <iostream>
#include <cstdio>
using namespace std;

int T;

int main()
{
	freopen("inp.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		int smax,stand=0,myFriend=0;
		cin>>smax;
		int audition[smax];
		string temp;
		cin>>temp;
		for(int j=0;j<=smax;j++)
		{
			audition[j]=(int)temp[j]-48;;
		}
		for(int j=0;j<=smax;j++)
		{
			if(audition[j]==0)
				continue;
			if(stand<j)
			{
				myFriend+=(j-stand);
				stand=j;
			}
			stand+=audition[j];
		}
		cout<<"Case #"<<i<<": "<<myFriend<<endl;
	}
}