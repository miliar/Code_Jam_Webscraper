#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
#define gc getchar
#define max 1005
void scan(int &x)
{
int flag=0;
register int c = gc();
if(c == '-') flag=1;
x = 0;
for(;(c<48 || c>57);c = gc());
for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
if(flag == 1)x=-x;
}

main()
{
	int t,n,input;
	scan(t);
	for(int k = 1;k<=t;k++)
	{
		int count = 0,count2 =0;
		scan(n);
		vector<int> v1,v2;
		for(int i =0;i<n;i++)
		{
			scan(input);
			v1.push_back(input);
			v2.push_back(input);
		}
		int count_alter = 0;
		sort(v1.begin(),v1.end());
		count = v1.back();
		int m = v1.back();
		while(m != 1)
		{
			count_alter++;
			sort(v1.begin(),v1.end());
			m = v1.back();
			if(m % 2 ==0)
			{
				v1.pop_back();
				v1.push_back(m/2);
				v1.push_back(m/2);
			}
			else
			{
			    
			    v1.pop_back();
			   if((m/2+1) %2 != 0)
				{
					v1.push_back(m/2+2);
					v1.push_back(m/2 - 1);
				}
				else{
				v1.push_back(m/2 + 1);
				v1.push_back(m/2);}
			}
			sort(v1.begin(),v1.end());
			if(count>count_alter + v1.back())
			{
				count = count_alter + v1.back();
			}
		}
		count_alter = 0;
		sort(v2.begin(),v2.end());
		count2 = v2.back();
		 m = v2.back();
		while(m != 1)
		{
			count_alter++;
			sort(v2.begin(),v2.end());
			m = v2.back();
			if(m % 2 ==0)
			{
				v2.pop_back();
				v2.push_back(m/2);
				v2.push_back(m/2);
			}
			else
			{
			    
			    v2.pop_back();
			  
				v2.push_back(m/2 + 1);
				v2.push_back(m/2);
			}
			sort(v2.begin(),v2.end());
			if(count2>count_alter + v2.back())
			{
				count2 = count_alter + v2.back();
			}
		}
		if(count>count2)
		    printf("Case #%d: %d\n",k,count2);
		else printf("Case #%d: %d\n",k,count);
	}
}
		