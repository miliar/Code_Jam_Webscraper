#include<iostream>

using namespace std;

int main()
{
	int t,n,o=0,stup,newaud,k;
	char a[1001];
	cin>>t;
	while(t--)
	{   o++;
		cin>>n;
		for(int i=0;i<=n;i++)
		cin>>a[i];
		stup=0;
		newaud=0;
		for(int i=0;i<=n;i++)
		{   k=(int)a[i]-48;
			if(k!=0)
			{if(i<=stup)
			stup=stup+k;
			else
			{
				newaud=newaud+(i-stup);
				stup=i+k;
			}
		}
	}
		cout<<"Case #"<<o<<": "<<newaud<<"\n";
		
	}
}
