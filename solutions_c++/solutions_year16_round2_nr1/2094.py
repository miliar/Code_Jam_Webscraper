#include<iostream>

using namespace std;

int main()
{	

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	    
	int t,c;
	
	cin>>t;
	
	c=t;
	
	while(t--)
	{
		string s;
		
		cin>>s;
		
		int alph[27]={0},num[10]={0};
		
		for(int i=0;s[i]!='\0';i++)
		{
			if(s[i]=='Z')
			num[0]++;
			if(s[i]=='W')
			num[2]++;
			if(s[i]=='U')
			num[4]++;
			if(s[i]=='X')
			num[6]++;
			if(s[i]=='G')
			num[8]++;
			
			if(s[i]=='O')
			num[1]++;
			if(s[i]=='R')
			num[3]++;
			if(s[i]=='F')
			num[5]++;
			if(s[i]=='V')
			num[7]++;
			if(s[i]=='I')
			num[9]++;
		}
		
		num[1]=num[1]-num[0]-num[2]-num[4];
		num[3]=num[3]-num[0]-num[4];
		num[5]=num[5]-num[4];
		num[7]=num[7]-num[5];
		num[9]=num[9]-num[5]-num[6]-num[8];
		
		cout<<"Case #"<<c-t<<": ";
		for(int i=0;i<10;i++)
		for(int j=1;j<=num[i];j++)
		cout<<i;
		
		cout<<endl;
	}
}
