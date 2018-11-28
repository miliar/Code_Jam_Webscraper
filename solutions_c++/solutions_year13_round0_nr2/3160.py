#include <iostream>
using namespace std;

int m[100][100];
int c[100][100];
int r[100][100];

int Judge1(int N,int M)
{
	for (int i=0;i<N;i++) 
	{			
		for(int j=0;j<M;j++)
		{
			int cur=m[i][j];
			if(i-1>=0)
			{
				if(m[i-1][j]>cur)
				{
					for(int k=0;k<M;k++)
					{
						if(m[i][k]>cur)
							return 0;
					}
				}
			}


			if(i+1<N)
			{
				if(m[i+1][j]>cur)
				{
					for(int k=0;k<M;k++)
					{
						if(m[i][k]>cur)
							return 0;
					}
				}
			}

			if(j-1>=0)
			{
				if(m[i][j-1]>cur)
				{
					for(int k=0;k<N;k++)
					{
						if(m[k][j]>cur)
							return 0;
					}
				}
			}

			if(j+1<M)
			{
				if(m[i][j+1]>cur)
				{
					for(int k=0;k<N;k++)
					{
						if(m[k][j]>cur)
							return 0;
					}
				}
			}
		}
	}
	
	return 1;
}


int Judge(int N,int M)
{
	for (int i=0;i<N;i++) 
	{			
		for(int j=0;j<M;j++)
		{			
			int cur=m[i][j];
			if(cur==1)
			{
				bool e=false,e1=false;
				for(int k=0;k<M;k++)
				{
					if(m[i][k]!=1)
					{
						e=true;
						break;
					}
				}
				if(e)
				{
					for(int k=0;k<N;k++)
					{
						if(m[k][j]!=1)
						{
							e1=true;
							break;
						}
					}
				}
				if(e&&e1)
					return 0;
			}
			
		}
	}
	
	return 1;
}


int Judge2(int N,int M)
{
	for (int i=0;i<N;i++) 
	{			
		for(int j=0;j<M;j++)
		{			
			int cur=m[i][j];

			bool e=false,e1=false;
			if(r[i][j]==1)
				e=true;
			else
			{
				for(int k=0;k<M;k++)
				{
					if(m[i][k]>cur)
					{
						e=true;
						break;
					}
					if(m[i][k]<cur)
					{
						r[i][k]=1;
					}
				}
			}
			if(e&&c[i][j]==0)
			{
					for(int k=0;k<N;k++)
					{
						if(m[k][j]>cur)
						{
							e1=true;
							break;
						}
						if(m[k][j]<cur)
						{
							c[k][j]=1;
						}
					}
			}
			else
			{
				e1=true;
			}
			if(e&&e1)
				return 0;

			
		}
	}
	
	return 1;
}


int main()
{	
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	//freopen("B-small-attempt4.in","r",stdin);freopen("B-small-attempt41.out","w",stdout);
	int testcase;
	int ans;
	
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		memset(m,0,sizeof(int)*100*100);
		memset(c,0,sizeof(int)*100*100);
		memset(r,0,sizeof(int)*100*100);
		printf("Case #%d: ",case_id);
		int N,M;
		cin>>N>>M;
		for (int i=0;i<N;i++) 
		{			
			for(int j=0;j<M;j++)
			{
				cin>>m[i][j];
			}
		}
		ans=Judge2(N,M);
		if(ans==1)
			printf("%s","YES");
		else
			printf("%s","NO");
		printf("\n");
	}

	return 0;
}

