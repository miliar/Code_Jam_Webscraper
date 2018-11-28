/*************************************************************************
	> File Name: 1.cpp
	> Author:hyh 
	> Mail: hyhdtcpelo@163.com 
	> Created Time: Sat 12 Apr 2014 11:02:59 AM CST
 ************************************************************************/

#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
	int T,i,j,n,y,k=0;
	cin>>T;
	ofstream fout("out.txt");
	while(T--)
	{
		vector<bool>mark(17,false);
		cin>>n;
		for(i=1;i<n;i++)
			for(j=1;j<=4;j++)
				cin>>y;
		for(i=1;i<=4;i++)
		{
			cin>>y;
			mark[y]=true;
		}
		for(i=n+1;i<=4;i++)
			for(j=1;j<=4;j++)
				cin>>y;
		cin>>n;
		int count=0,ans=-1;
		for(i=1;i<n;i++)
			for(j=1;j<=4;j++)
				cin>>y;
		for(i=1;i<=4;i++)
		{
			cin>>y;
			if(mark[y])
			{
				count++;
				ans=y;
			}
		}
		for(i=n+1;i<=4;i++)
			for(j=1;j<=4;j++)
				cin>>y;
		if(count==0)
			fout<<"Case #"<<++k<<": "<<"Volunteer cheated!"<<endl;
		if(count==1)
			fout<<"Case #"<<++k<<": "<<ans<<endl;
		if(count>1)
			fout<<"Case #"<<++k<<": "<<"Bad magician!"<<endl;
	}
	return 0;
	
}
