#include <iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;

	for(int j=0;j<t;j++)
	{
		int p,q;
		cin>>p;
		char a;
		cin>>a;
		cin>>q;
		int i = 1;
		int x = 0;

		bool notpos = false;
		while(true)
		{
			if(i>=1024)
			{
				notpos = true;	
				break;
			}	
			else if(q==i)break;
			i = i*2;
			x+=1;
		}	
int y = 0;
		if(!notpos)
		{	
		i = 2;
		

		while(true)
		{
			if(p<i)break;
			i = i*2;
			y+=1;
		}	
		}

		if(notpos)cout<<"Case #"<<j+1<<": "<<"impossible"<<endl;
		else cout<<"Case #"<<j+1<<": "<<x-y<<endl;


	}




}