#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	ofstream myfile;
	myfile.open("aoutput.txt");
	int pos[4];
	int cases,count,ans;
	cin>>cases;
	for(int i=0;i<cases;i++)
	{
		count = 0;
		ans = 0;
		int temp,a;
		cin>>temp;
		for(int x=0;x<4;x++)
		{
			for(int y=0;y<4;y++)
			{
				if(x!=temp-1)
				cin>>a;
				else if(x==temp-1)
				cin>>pos[y];
			}
		}
		cin>>temp;
		for(int x=0;x<4;x++)
		{
			for(int y=0;y<4;y++)
			{
				if(x!=temp-1)
				{
				cin>>a;
				cin.clear();
				}
				else if(x==temp-1)
				{
					cin>>a;
					cin.clear();
					for(int z=0;z<4;z++)
					{
					if(a==pos[z])
						{
						count++;
						ans=a;
						}
					}
				}
			}
		}
		if(count==1)
		{
			myfile<<"Case #"<<i+1<<": "<<ans<<endl;
		}
		else if(count>1)
		{
			myfile<<"Case #"<<i+1<<": Bad Magician!"<<endl;
		}
		else if(count==0)
		{
			myfile<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}
	}
	myfile.close();
	return 0;
}
