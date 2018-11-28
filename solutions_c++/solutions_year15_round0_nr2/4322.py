#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>

using namespace std;

int main()
{
	int t;
	cin>>t;
	
	int tt;
	for(tt = 1; tt<=t; tt++)
	{
		
		int d;
		cin>>d;
		
		int i;
		vector<int> p;
		for(i=0;i<d;i++)
		{
			int l;
			cin>>l;
			p.push_back(l);
		}
		int fans = 0;
		int ans = 0;
		bool fd = false;
		for(ans = 1; ans<=9;ans++)
		{
			int mask = 0;
			
			
			do
			{
				vector<int> pp;
				for(i=0;i<p.size();i++)
					pp.push_back(p[i]);
				sort(pp.rbegin(),pp.rend());
				
				for(i=0;i<ans;i++)
				{
					if((mask&(1<<i))!=0)
					{
						pp.push_back(pp[0]/2);
						pp[0] = ceil(pp[0]/2.0);
						sort(pp.rbegin(),pp.rend());
					}
					else
					{
						int j;
						for(j=0;j<pp.size();j++)
						{
							if(pp[j] == 0)
								break;
							pp[j]--;
							
						}
						
						
					}
					
				}
				if(pp[0] == 0)
				{
					fd  = true;
					break;
					
				}
				mask++;
			}
			while(mask<pow(2, ans));
			if(fd)
				break;
		}
		fans = ans;
		
		ans = 0;
		fd = false;
		for(ans = 1; ans<=9;ans++)
		{
			int mask = 0;
			
			
			do
			{
				vector<int> pp;
				for(i=0;i<p.size();i++)
					pp.push_back(p[i]);
				sort(pp.rbegin(),pp.rend());
				
				for(i=0;i<ans;i++)
				{
					if((mask&(1<<i))!=0)
					{
						if(pp[0]<=7)
						{
							pp.push_back(pp[0]/2);
							pp[0] = ceil(pp[0]/2.0);
							sort(pp.rbegin(),pp.rend());
						}
						else if(pp[0]==8)
						{
							pp.push_back(3);
							pp[0] = 5;
							sort(pp.rbegin(),pp.rend());
						}
						else 
						{
							pp.push_back(3);
							pp[0] = 6;
							sort(pp.rbegin(),pp.rend());
						}
					}
					else
					{
						int j;
						for(j=0;j<pp.size();j++)
						{
							if(pp[j] == 0)
								break;
							pp[j]--;
							
						}
						
						
					}
					
				}
				if(pp[0] == 0)
				{
					fd  = true;
					break;
					
				}
				mask++;
			}
			while(mask<pow(2, ans));
			if(fd)
				break;
		}
		fans = min(ans, fans);
		cout<<"Case #"<<tt<<": "<<fans<<endl;
	}
}