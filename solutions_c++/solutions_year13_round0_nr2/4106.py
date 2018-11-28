#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
#include<fstream>
using namespace std;
int a[105][105];
int main()
{
	int i,j,t,f=-1,flag=0,ij=1,val,val2,m,n,k;
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	fin>>t;
	//scanf("%d",&t);
	while(t--)
	{
		fin>>m>>n;
		//scanf("%d%d",&m,&n);
		flag=0;
		for(i=0;i<m;i++)
		for(j=0;j<n;j++)
		fin>>a[i][j];
		//scanf("%d",&a[i][j]);
		for(i=0;i<m;i++)
		{
			for(j=0;j<n;j++)
			{
				val=-1;
				val2=-1;
				for(k=0;k<n;k++)
				val=max(val,a[i][k]);
				for(k=0;k<m;k++)
				val2=max(val2,a[k][j]);
				if(val>a[i][j]&&val2>a[i][j])
				{
					flag=1;
					break;
				}
			}
		}
		fout<<"Case #"<<ij++<<": "; 
		//printf("Case #%d: ",ij++);
		if(flag==1)
		fout<<"NO\n";//printf("NO\n");
		else
		fout<<"YES\n";//printf("YES\n");
	}	
	fout.close();
	fin.close();
	return 0;
}
