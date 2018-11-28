#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
int multi(int x, int y)
{
	bool reverse=false;
	int res[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
	if (x<0)
	{
		x=-x;
		reverse=!reverse;
	}
	if (y<0)
	{
		y=-y;
		reverse=!reverse;
	}
	if (reverse)
		return -res[x-1][y-1];
	else
		return res[x-1][y-1];
}
int main()
{
//	freopen("in.txt","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=0;t<T;t++)
	{
		cout<<"Case #"<<t+1<<": ";
		bool res=false;
		long l,x;
		string s;
		int num[1000000];
		cin>>l>>x>>s;
		if (x>20)
			x=16+x%4;
		for (int i=0;i<x;i++)
		{
			for (int j=0;j<l;j++)
			{
				num[l*i+j]=s[j]-'i'+2;
			}
		}
		int pd=1;
		for (int i=0;i<x*l;i++)
		{
			pd=multi(pd,num[i]);
		}
		if (pd!=-1)
			res=false;
		else
		{
			int pdi=1;
			for (int i=0;!res && i<x*l;i++)
			{
				pdi=multi(pdi,num[i]);
				if (pdi==2)
				{
					int pdj=1;
					for (int j=i+1;!res && j<x*l;j++)
					{
						pdj=multi(pdj,num[j]);
						if (pdj==3)
						{
							int pdk=1;
							for (int k=j+1;k<x*l;k++)
							{
								pdk=multi(pdk,num[k]);
							}					
							if (pdk==4)
							{
								res=true;
							}
						}
					}
				}
			}
		}
		if (res)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}
