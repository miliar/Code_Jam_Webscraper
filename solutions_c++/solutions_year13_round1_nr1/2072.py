#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int T;
	int r,t;
	
	cin>>T;
	for(int x=1;x<=T;x++)
	{
			cin>>r>>t;
			int y=r*2+1;
			int sum=y;
			int count=0;
			while(sum<=t)
			{
				count++;
				y += 4;
				sum +=y;
			}
			cout<<"Case #"<<x<<": "<<count<<endl;	
	}
return 0;
}
