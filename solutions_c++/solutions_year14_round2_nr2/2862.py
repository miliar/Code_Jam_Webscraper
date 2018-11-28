#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc;
	int ca=1;
	scanf("%d",&tc);
	//cout<<(2&2)<endl;
	while(tc--)
	{
		int a,b,c;
		int res=0;
		scanf("%d %d %d",&a,&b,&c);
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				int x=i&j;
				if(x<c)
				{
					res++;
	//				cout<<i<<" "<<j<<" "<<x<<endl;
				}
			}
		}
		cout<<"Case #"<<ca++<<": "<<res<<endl;
	}
}