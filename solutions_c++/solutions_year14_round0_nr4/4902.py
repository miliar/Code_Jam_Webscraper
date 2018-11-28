#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
	ofstream myfile;
	myfile.open("doutput.txt");
	vector<double> n,k;
	vector<double>::iterator it;
	int cases,blocks,dwar,war;//dwar is number of wins when playing deceitful war and war is number of wins playing normal war
	cin>>cases;
	for(int a=0;a<cases;a++)
	{	
		n.clear();
		k.clear();
		cin>>blocks;
		dwar=0;
		war=blocks;
		for(int i=0;i<blocks;i++)
		{
			double temp;
			cin>>temp;
			cin.clear();
			n.push_back(temp);
		}
		sort(n.begin(),n.end());
		for(int i=0;i<blocks;i++)
		{
			double temp;
			cin>>temp;
			cin.clear();
			k.push_back(temp);
		}
		sort(k.begin(),k.end());
		int x=0,y=0;
		reverse(n.begin(),n.end());
		reverse(k.begin(),k.end());
		while(x<blocks && y<blocks)
		{
			if(n[x]>k[y])
			{ 
				dwar++;
				x++;
				y++;
			}
			
			else if(n[x]<k[y])
			{
				y++;
			}
		}
		
		x=0;
		y=0;
		while(x<blocks && y<blocks)
		{
			if(n[x]>k[y])
			{
				x++;
			}
			
			else if(n[x]<k[y])
			{
				war--;
				y++;
				x++;
			}
		}
		
		myfile<<"Case #"<<a+1<<": "<<dwar<<" "<<war<<endl;
	}
	return 0;
}
