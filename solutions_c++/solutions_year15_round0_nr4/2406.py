#include<iostream>
using namespace std;
int main()
{
	int t,x,r,c;
	int no=0;
	char g[] = {"GABRIEL"};
	char ric[] = {"RICHARD"};
	cin>>t;
	while(t--)
	{
		cin>>x>>r>>c;
		no++;
		cout<<"Case #"<<no<<": ";
		if(r==1 && c==1)
		{
			if(x==1)
				cout<<g<<endl;
			else
				cout<<ric<<endl;
		}
		
		if( (r==1 && c==2) || (r==2 && c==1) )
		{
			if(x==1 || x==2)
				cout<<g<<endl;
			else
				cout<<ric<<endl;
		}
		
		if((r==1 && c==3) || (r==3 && c==1))
		{
			if(x==1)
				cout<<g<<endl;
			else
				cout<<ric<<endl;			
		}

		if((r==1 && c==4) || (r==4 && c==1))
		{
			if(x==1 || x==2)
				cout<<g<<endl;
			else
				cout<<ric<<endl;
		}
		
		if(r==2 && c==2)
		{
			if(x==1 || x==2)
				cout<<g<<endl;
			else
				cout<<ric<<endl;		
		}

		if((r==2 && c==3) || (r==3 && c==2))
		{
			if(x==4)
				cout<<ric<<endl;
			else
				cout<<g<<endl;
		}
	
		if((r==2 && c==4) || (r==4 && c==2))
		{
			if(x==1 || x==2)
				cout<<g<<endl;
			else
				cout<<ric<<endl;		
		}

		if(r==3 && c==3)	
		{
			if(x==1 || x==3)
				cout<<g<<endl;
			else
				cout<<ric<<endl;
		}
		
		if((r==3 && c==4) || (r==4 && c==3))
			cout<<g<<endl;
		
		if(r==4 && c==4)
		{
			if(x==3)
				cout<<ric<<endl;
			else
				cout<<g<<endl;
		}
	}
}
