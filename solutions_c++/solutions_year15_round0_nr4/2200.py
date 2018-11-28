#include <bits/stdc++.h>
using namespace std;

int main()
{
	int test;
	cin>>test;
	for(int z=1;z<=test;z++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		bool richard;
		if(x==1)
		{
			richard = 0;
		}
		if(x==2)
		{
			if(r*c % 2 == 0)
			{
				richard = 0;
			}
			else richard = 1;
		}
		if(x==3)
		{
			if(r*c % 3 != 0)
			{
				richard=1;
			}	
			else 
			{
				if(r!=3)swap(r,c);
				if(c==1)richard=1;
				if(c==2)richard =0;
				if(c==3)richard=0; // .
				if(c==4)richard=0;
			}
		}
		if(x==4)
		{
			if(r*c % 4 != 0)
			{
				richard=1;
			}
			else
			{
				if(r == 2 && c == 2)
				{
					richard=1;
				}
				else 
				{
					if(r!= 4 )swap(r,c);
					if(c==1)richard=1;
					if(c==2)richard=1;
					if(c==3)richard=0;
					if(c==4)  
					{
						richard = 0; // . 
					}
				}
			}
		}
		if(richard)
			cout<<"Case #"<<z<<": RICHARD"<<endl;
		else 
			cout<<"Case #"<<z<<": GABRIEL"<<endl;
	}
}
