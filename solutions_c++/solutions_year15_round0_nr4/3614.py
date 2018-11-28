#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
	ofstream out("file.txt");
	int t;
	scanf("%d",&t);
	int i=0;
	int arr[]={0,1,2,3,3,4,4,5,5,5};
	while(++i<=t)
	{
		int x,r,c;
		scanf("%d%d%d",&x,&r,&c);
		int area=r*c;
		string s;
		if(x==1)
		{
			s=" GABRIEL";
		}
		else if(x==2)
		{
			if(area%2==0)
			{
					s="GABRIEL";
			}
			else
			{
				s="RICHARD";
			}
		}
		else if(x==3)
		{
			if(area==6 || area==9 || area==12)
			{
					s="GABRIEL";
			}
			else
			{
				s="RICHARD";
			}
		}
		else if(x==4)
		{
			if(area==12 || area==16)
			{
					s="GABRIEL";
			}
			else
			{
					s="RICHARD";
			}
		}
		out<<"Case #"<< i <<": "<< s<< endl;
	}
}

