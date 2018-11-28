#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	char ch[1];
	cin.getline(ch,1,'\n');//For escaping first '\n' character.
	int count=0;
	int R[t];
	while(count<t)
	{
		bool bit[100];
		char in[120];
		cin.getline(in,120,'\n');
		int length = 0;
		while(in[length]!='\0') 
		{
			if(in[length]=='-')
			bit[length]=false;
			else
			bit[length]=true;
			length ++;
		}
		int p =0;
		int c = 1;
		int cn = 0;
		if(length==1)
		{
			if(!bit[0])
			++cn;
		}
		else
		{
			while(c<length)
			{
				while(bit[p] == bit[c]&&c<length)
				{
					c++;
				}
				if(c==length)
				{
					if(!bit[0])
					++cn;
				}
				else
				{
					for(int i=0;i<c;i++)
					bit[i]=!bit[i];	
					++cn;
					p=c;
				}	
			}
		
		}
		R[count] = cn;
		++count;	
	}
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": "<<R[i]<<endl;
	}
}
