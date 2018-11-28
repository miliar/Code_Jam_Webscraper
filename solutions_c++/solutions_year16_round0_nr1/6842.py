#include<iostream>
#include<string>
using namespace std;

bool allNumberSeen(bool * numberSeen)
{
	for(int i=0;i<10;i++)
		if(numberSeen[i]==false)
			return false;
	return true;
}
void lastNumber(int N)
{
	bool numberSeen[10];
	for(int i=0;i<10;i++)
		numberSeen[i]=false;
	
	if(N!=0)
	{
		int temp,n=N;
		while(allNumberSeen(numberSeen)==false)
		{
			temp=n;
			while(temp!=0)
			{
				int rem = temp%10;
				numberSeen[rem]=true;
				temp=temp/10;
			}
			n=n+N;
		}
		cout<<n-N;
	}
	else
		cout<<"INSOMNIA";
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,N;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>N;
		cout<<"Case #"<<i<<": ";
		lastNumber(N);
		cout<<endl;
	}
}
