#include<iostream>
using namespace std;
int ar[100][100],a[103];
int fun(int y,int n,int m)
{int t,m1,i,j,fl;


	fl=0;

		for(j=1;j<m-1;j++)
		{fl=0;
			if(ar[0][j]==y||ar[0][j]==0)
			{for(i=0;i<n;i++)
				{if(ar[i][j]==y||ar[i][j]==0)
					{}
				else {fl=1;break;}
				}
			if(fl==0) {for(i=0;i<n;i++) ar[i][j]=0;}
			}
		}
		

for(i=1;i<n-1;i++)
			{fl=0;if(ar[i][0]==y||ar[i][0]==0)
			{for(j=0;j<m;j++)
				{if(ar[i][j]==y||ar[i][j]==0)
					{}
				else {fl=1;break;}
				}
			
			if(fl==0) {for(j=0;j<m;j++) ar[i][j]=0;}}
			}



if(ar[0][0]==y||ar[0][0]==0)
		{fl=0;
			for(i=0;i<n;i++)
						{if(ar[i][0]==y||ar[i][0]==0)
							{}
						else{fl=1;break;}						
						}
		if(fl==0) {for(i=0;i<n;i++) ar[i][0]=0;} 
			fl=0;		

			for(j=0;j<m;j++)
						{if(ar[0][j]==y||ar[0][j]==0)
							{}
						else {fl=1;break;}
						}
			if(fl==0){for(j=0;j<m;j++) ar[0][j]=0;}		
		}
if(ar[n-1][m-1]==y||ar[n-1][m-1]==0)
		{		fl=0;
				for(i=0;i<n;i++)
						{if(ar[i][m-1]==y||ar[i][m-1]==0)
							{}
						else{fl=1;break;}						
						}
				if(fl==0){for(i=0;i<n;i++) ar[i][m-1]=0;}
				fl=0;
				for(j=0;j<m;j++)
						{if(ar[n-1][j]==y||ar[n-1][j]==0)
							{}
						else {fl=1;break;}
						}
				if(fl==0) {for(j=0;j<m;j++) ar[n-1][j]=0;}




		}



for(i=0;i<n;i++)
		{for(j=0;j<m;j++)
			{if(ar[i][j]==y)
				{return 0;}
			}
		}

return 1;
}


int main()
{int t,i,i1,j,k,n,m;
cin>>t;
for(i=0;i<102;i++)
	a[i]=0;
for(i1=0;i1<t;i1++)
	{cin>>n;
	cin>>m;
		for(i=0;i<n;i++)
			{for(j=0;j<m;j++)
				{cin>>ar[i][j];
				a[ar[i][j]]=1;		
				}

			}
		for(int u=0;u<102;u++)
		{if(a[u]!=0)	

		{
j=fun(u,n,m);

		if(j==0) break;		
		}}
	if(j==0)
		{cout<<"Case #"<<i1+1<<": "<<"NO"<<endl;}
	else {cout<<"Case #"<<i1+1<<": "<<"YES"<<endl;}	
	}	
}
	

