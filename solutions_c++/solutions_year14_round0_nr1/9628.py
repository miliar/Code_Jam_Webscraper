#include<cstdio>
#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<ctime>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<set>
#include<map>
using namespace std;

#define LL long long

int main() 
{
	int a[4],b[4],c[4],t,ans1,ans2,i,j,x=1,d,cou=0;
	//freopen("input.txt","r",stdin);
	//freopen("output1.txt","w",stdout);
	
	cin>>t;
	while(x<=t)
	{
		cin>>ans1;
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(i==(ans1-1))
					cin>>a[j];
				else
					cin>>d;
			}
		}
		cin>>ans2;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(i==(ans2-1))
					cin>>b[j];
				else
					cin>>d;
			}
		}
		sort(a,a+4);
		sort(b,b+4);
		
		
		i=0;j=0,cou=0;
		while(i<4 && j<4)
		{
			if(a[i]>b[j])j++;
			else if(a[i]<b[j])i++;
			else 
			{
				c[cou]=a[i];
				cou++;i++;j++;
			}
				
		}
		if(cou==0)
		{
			cout<<"Case #"<<x<<": Volunteer cheated!"<<endl;
		}
		else if(cou==1)
		{
			cout<<"Case #"<<x<<": "<<c[0]<<endl;
		}
		else if (cou>1)
		{
			cout<<"Case #"<<x<<": Bad magician!"<<endl;
		}
		
		x++;
		
		
	}
	
    return 0;
}
