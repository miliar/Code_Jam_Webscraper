#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int i,j,t;
	ifstream data("input");
	data>>t;
	
	for(i=0;i<t;i++)
	{
		int x,r,c,y=0;
		data>>x>>r>>c;
		if(x>r*c)
		y++;
		else if((r*c)%x!=0)
		y++;
		else if(x>r&&r>=c)
		y++;
		else if(x>c&&c>r)
		y++;
		else if((x==3&&r==3&&c==1)||(x==4&&r==4&&c==1)||(x==4&&r==4&&c==2)||(x==3&&r==1&&c==3)||(x==4&&r==1&&c==4)||(x==4&&r==2&&c==4))
		y++;
		
		if(y==1)
		{
		fstream result;
		result.open("output",ios::app|ios::out);
		result<<"Case #"<<(i+1)<<": "<<"RICHARD"<<"\n";
	    }
	    else
	    {
		fstream result;
		result.open("output",ios::app|ios::out);
		result<<"Case #"<<(i+1)<<": "<<"GABRIEL"<<"\n";
	    }
	}
	
}
