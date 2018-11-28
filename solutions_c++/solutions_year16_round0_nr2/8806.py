#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for (int l = 1; l <=t; ++l)
	{
	string s;
	cin>>s;
	int count=0;
	int size = s.size();
		bool t2=0,t3=0;
		char x=s[size-1];
		int x1=size-1;
		while(x1!=0)
		{	
			for(int i=x1;i>=0;i--)
			{
				if(s[i]!=x)
				{
					x1=i;
					t2=1;
					break;
				}
			}
			if(t2==0)
				x1=0;
			if(t2==1)
			{
			count++;
			for(int i=0;i<=x1;i++)
			{
				if(s[i]=='+')
					s[i]='-';
				else
					s[i]='+';
			}
			//x1--;
			t2=0;
		}
		}
		if(x=='+')
			cout<<"Case #"<<l<<": "<<count<<endl;
		else
			cout<<"Case #"<<l<<": "<<count+1<<endl;
	}
	return 0;
}
