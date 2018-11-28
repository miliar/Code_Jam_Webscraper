#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main() 
{
	freopen("A-large.in","r",stdin);
	freopen("Output1-2.txt","w",stdout);
	int T;
	cin>>T; // T [1,100]
	for(int i=1; i<=T; i++)
	{
		string str;
		cin>>str;
		cout<<"Case #"<<i<<": ";
		if(str=="0")
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		reverse(str.begin(),str.end());
		int L=str.length();
		int LDigi = L;
		int Digi[100]={0};		
		int Flag=0, digitFlag[10]={0};
		int d=0, temsum=0, temnum=0;
		for(int j=L-1; j>=0; j--)
		{
			if(digitFlag[(str[j]-'0')]==0)
			{
				digitFlag[(str[j]-'0')]=1;
				Flag += 1;
			}
		}
		while(Flag!=10)
		{
			for(int j=0; j<LDigi; j++)
			{
				if(j>L-1) temnum=0;
				else temnum=(str[j]-'0');
				temsum = Digi[j] + temnum + d;
				Digi[j]= temsum % 10;
				d = temsum / 10;
				if(digitFlag[Digi[j]]==0)
				{
					digitFlag[Digi[j]]=1;
					Flag += 1;
				}
				if(j==LDigi-1 && d>0) LDigi++;
			}
		}
		for(int j=LDigi-1; j>=0; j--)
		{
			cout<<Digi[j];
		}
		cout<<endl;
	}
	return 0;
}
