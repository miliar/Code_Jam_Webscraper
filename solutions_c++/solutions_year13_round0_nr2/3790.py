#include<stdio.h>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int a[100][100],j,it,T,i,m,s,n,k,e,q;
pair <int,int> p[1000000];
//char s[100][100];
bool wx,prt;
int main()
{
	 freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin>>T;
	for(it=0;it<T;it++)
	{
		prt=true;
		wx=true;
		cin>>n>>m;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				cin>>a[i][j];

		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				int q=a[i][j];
				
					prt=true;
					for(s=0;s<m;s++)
						if(a[i][s]>q)
						{
							prt=false;
							break;
						}

					if(!prt)
					{
						prt=true;
						for(s=0;s<n;s++)
						if(a[s][j]>q)
						{
							prt=false;
							break;
						}
						if(!prt){
							cout<<"Case #"<<it+1<<": NO"<<endl;
							wx=false;
							i=n;
							j=m;
						}
					}

			}		

			if(wx)
				cout<<"Case #"<<it+1<<": YES"<<endl;
							

	}
	return 0;
}