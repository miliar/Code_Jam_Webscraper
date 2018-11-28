#include<iostream>
#include<stdio.h>
#include<vector>
#include<map>
#include<set>
using namespace std;



int main()
{
int test=0;

scanf("%d",&test);
int t_=0;
int n=0,m=0;

int my_arr[100][100];
int myfinal[100][100];
int rm_maxx[100];
int cl_maxx[100];

while(t_<test)
{
	t_++;
	scanf("%d%d",&n,&m);

	for(int i=0;i<100;i++)
	{
		rm_maxx[i]=0;
		cl_maxx[i]=0;
	}
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
			{
				scanf("%d",&my_arr[i][j]);
				//cout<<my_arr[i][j]<<" ";
				if(rm_maxx[i]<my_arr[i][j])rm_maxx[i]=my_arr[i][j];
			}
	}

	for(int i=0;i<m;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(cl_maxx[i]<my_arr[j][i])cl_maxx[i]=my_arr[j][i];
		}
	}

	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
			myfinal[i][j]=rm_maxx[i];
	}

	for(int i=0;i<m;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(myfinal[j][i]>cl_maxx[i])myfinal[j][i]=cl_maxx[i];
		}
	}

	int flag=1;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(my_arr[i][j]!=myfinal[i][j])
			{
				flag=0;break;
			}
		}
		if(flag==0)break;
	}
	if(flag==0)
		printf("Case #%d: NO\n",t_);
	else if(flag==1)
		printf("Case #%d: YES\n",t_);
	}
	return 0;
}
