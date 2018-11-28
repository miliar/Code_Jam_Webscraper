#include<cstdio>
#include<iostream>

using namespace std;

//const float pi=3.14;

void main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a_small.out","w",stdout);
	
	int T;
	__int64 r,t,s;
	int count;
	//bool flag;
	cin>>T;
	for(int i=0;i!=T;++i)
	{
		
		scanf("%I64d",&r);
		scanf("%I64d",&t);
	//	flag=true;
		s=0;
		count=0;
		while(true)
		{
			s+=(r+1)*(r+1)-(r)*(r);
			r+=2;
			if(s<=t)
			{
				count++;
			}
			else break;
		}
		if(count==0)
			cout<<"Case #"<<i+1<<": 1"<<endl;  
		else
			cout<<"Case #"<<i+1<<": "<<count<<endl; 
	}
	return ;
	

}
