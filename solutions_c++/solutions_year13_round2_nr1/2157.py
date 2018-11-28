#include<iostream>
#include<cstdio>
#include<fstream>
#include<stdlib.h>
#include<string.h>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
int a[110],n,flag=0;
int dfs(int s,int j,int count)
{
if(j==n)
{
		flag=1;
	return count;

}
else
  {
  	if(s>a[j])
  	dfs(s+a[j],j+1,count);
  	else
  	{
  	int k=min(count+n-j,dfs(2*s-1,j,count+1));
  	if(flag==1)
  	return k;
  	if(k==count+n-j)
  	{
  	j=n;
  	return k;
  	}
  	}
  }
	
}
int main()
{
	fstream fin,fout;
	fin.open("in.txt");
	fout.open("out.txt");
	int t,s,j,count=0,k;
	fin>>t;

	for(int i=1;i<=t;i++)
	{
		
		fin>>s>>n;
		for(j=0;j<n;j++)
		fin>>a[j];
		sort(a,a+n);
			flag=0;
			fout<<"Case #"<<i<<": ";
		if(s==1&&a[0]>=s)
		fout<<n<<"\n";
		else
		{
		k=dfs(s,0,0);
	
		
		fout<<k<<"\n";
		}
	}
	return 0;
	
}
