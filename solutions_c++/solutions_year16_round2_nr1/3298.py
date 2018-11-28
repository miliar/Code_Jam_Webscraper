#include<iostream>
using namespace std;

int main()
{
	int t,count(1);
	cin>>t;
	char in[2002];
	cin.getline(in,2,'\n');
	while(count<=t)
	{
		cin.getline(in,2001,'\n');
	 	int freq[15]={0};
		int i=0;
		while(in[i]!='\0')
		{
			if(in[i]=='E')
			{
				freq[0]++;
			}
			else if(in[i]=='F')
			freq[1]++;
			else if(in[i]=='G')
			{
				freq[2]++;
				freq[0]--;
				freq[4]--;
				freq[3]--;
				freq[9]--;
			}
			else if(in[i]=='H')
			{
				freq[3]++;
			}
			else if(in[i]=='I')
			{
				freq[4]++;
			}
			else if(in[i]=='N')
			{
				freq[5]++;
			}
			else if(in[i]=='O')
			{
				freq[6]++;
			}
			else if(in[i]=='R')
			{
				freq[7]++;
			}
			else if(in[i]=='S')
			{
				freq[8]++;
			}
			else if(in[i]=='T')
			{
				freq[9]++;
			}
			else if(in[i]=='U')
			{
				freq[10]++;
				freq[1]--;
				freq[6]--;
				freq[7]--;
			}
			else if(in[i]=='V')
			{
				freq[11]++;
			}
			else if(in[i]=='W')
			{
				freq[12]++;
				freq[9]--;
				freq[6]--;
			}
			else if(in[i]=='X')
			{
				freq[13]++;
				freq[8]--;
				freq[4]--;
			}
			else if(in[i]=='Z')
			{
				freq[14]++;
				freq[0]--;
				freq[7]--;
				freq[6]--;
			}
			i++;
		}
		freq[5]-=freq[6];
		freq[0]-=freq[6];
		freq[11]-=freq[8];
		freq[5]-=freq[8];
		cout<<"Case #"<<count<<": ";
		for(i=0;i<freq[14];i++)
		cout<<0;
		for(i=0;i<freq[6];i++)
		cout<<1;
		for(i=0;i<freq[12];i++)
		cout<<2;
		for(i=0;i<freq[9];i++)
		cout<<3;
		for(i=0;i<freq[10];i++)
		cout<<4;
		for(i=0;i<freq[11];i++)
		cout<<5;
		for(i=0;i<freq[13];i++)
		cout<<6;
		for(i=0;i<freq[8];i++)
		cout<<7;
		for(i=0;i<freq[2];i++)
		cout<<8;
		freq[5] = freq[5]/2;
		for(i=0;i<freq[5];i++)
		cout<<9;
		cout<<endl;
		count++;
	}
}
