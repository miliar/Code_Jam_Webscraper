#include<iostream>
#include<stdio.h>
#include<vector>
#include<sstream>
#include<string>
#include<string.h>
#include<cstring>
#include<math.h>
using namespace std;

int main () 
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	bool stop;
	stringstream ss;
	string s;
	int n,x,y,counter=0,c=0,temp;
	cin>>n;
	while(n--)
	{
		counter=0;
		cin>>x>>y;
		for(int i=x;i<=y;i++)
		{
			temp=sqrt(i);
			ss.clear();
			if(i==temp*temp)
			{
				ss<<i;
				ss>>s;
				stop=0;
				for(int i=0,j=s.size()-1;i<j;i++,j--)
				{
					if(s[i]!=s[j])
					{
						stop=1;
						break;
					}
				}
				if(stop)
					continue;
				ss.clear();
				ss<<temp;
				ss>>s;
				stop =0;
				for(int i=0,j=s.size()-1;i<j;i++,j--)
				{
					if(s[i]!=s[j])
					{
						stop=1;
						break;
					}
				}
				if(stop)
					continue;
				counter++;
			}
		}
		printf("Case #%d: %d\n",++c,counter);
	}
}