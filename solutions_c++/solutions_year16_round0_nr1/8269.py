#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cstdio>

using namespace std;


bool find(char * t,int len,char c)
{
	for(int i = 0; i < len ; i++)
	{
		if(t[i] == c)
			return true;
	}
	
	return false;
}


int main()
{
	long n;
	int /*d[10],*/c,len;

	
	cin>>c;
	
	for(int i = 0; i < c; i++)
	{
		cin>>n;
		
		
		if(n == 0)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
		else
		{
			int d[10];
			for(int j = 0; j < 10; j++)
			{
				d[j] = 0;
			}
		
			
			int nb = 1;
			while(true)
			{
				char tmp[10000];
				sprintf(tmp,"%ld",n*nb);
				//cout<<"("<<tmp<<")"<<endl;
				len = strlen(tmp);
				
				
				for(int j = 0; j < len; j++)
				{
					if(find(tmp,len,'0'))
						d[0] = 1;
					if(find(tmp,len,'1'))
						d[1] = 1;
					if(find(tmp,len,'2'))
						d[2] = 1;
					if(find(tmp,len,'3'))
						d[3] = 1;
					if(find(tmp,len,'4'))
						d[4] = 1;
					if(find(tmp,len,'5'))
						d[5] = 1;
					if(find(tmp,len,'6'))
						d[6] = 1;
					if(find(tmp,len,'7'))
						d[7] = 1;
					if(find(tmp,len,'8'))
						d[8] = 1;
					if(find(tmp,len,'9'))
						d[9] = 1;
					
				}
				
				bool test = false;
				for(int j = 0; j < 10; j++)
				{
					if(d[j] == 0)
					{
						test = true;
						break;
					}
				}
				
				if(test == false)
				{
					cout<<"Case #"<<i+1<<": "<<tmp<<endl;
					break;
				}
				
				nb++;
			}
		
		}
		
		cin.clear();
		
	}
	
	return 0;
	
}