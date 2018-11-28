#include <bits/stdc++.h>
using namespace std;
#define MAX 250
int n , t , i , j , A[MAX] , li[MAX][MAX] ,size[MAX],terminal[MAX] ,used[MAX],k,vis[MAX];
long long DP[MAX][MAX][MAX];

int gcd(int a , int b)
{
	if(a<b)return gcd(b,a);
	if(b==0)return a;
	else return gcd(b,a%b);
}
void myrandom()
{
	int hcf = 0 ,count=0 ,x=rand()%n;
	while(hcf!=1 && count<n)
	{
		hcf=G[hcf][A[AR[x%n]]];
		count++;
		x++;
	}
	/*if(count%2) loose+=(fact[count]/fact[count]);
	else win+=(fact[count]/fact[count]);*/
	if(count%2) loose++;
	else win++;
	//return !(count%2);
}
int check (int c)
{
	int ans=0;
	for(int i =0;i<n;i++)
	{
		if(used[A[i]])ans=1;
		else continue;
		for(int j=0;j<k;j++)
		{
			if(li[j][A[i]]&&size[j]%2==0)
			{
				ans=0;break;
			}
		}
		//if(ans=1)printf(":O :O :( :'( %d\n",A[i] );
		if(ans)break;
	}
	//printf("HI: %d %d\n",ans,c );
	if(ans&&c%2==1)return 0;
	if(ans&&c%2==0)return 1;
	for(int i=0;i<n;i++)
	{
		memset(vis,false,sizeof vis);
		if(!used[A[i]])continue;
		else used[A[i]]--;
		for(int j=0;j<k;j++)
		{
			if(li[j][A[i]])li[j][A[i]]--,size[j]--,vis[j]++;
		}
		int cur = check(c+1);
		if(cur)return 1;
		for(int j=0;j<k;j++)
		{
			if(vis[j])li[j][A[i]]++,size[j]++;
		}
		used[A[i]]++;
	}
	return 0;
}
int main()
{
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		memset(li , false , sizeof li);
		memset(used , false , sizeof used);
		memset(size , false , sizeof size);
		memset(terminal , false , sizeof terminal);
		for(i=0;i<n;i++)
		{
			scanf("%d",&A[i]);
			used[A[i]]++;
		}
		used[1]=0;
		for(i=2;i<MAX;i++)
		{
			int GCD=0;
			for(j=0;j<n;j++)
			{
				if(gcd(A[j],i)!=1) GCD=gcd(GCD,A[j]);
			}
			if(GCD == i){terminal[i]++;}
		}
		k=0;
		for(i=2;i<MAX;i++)
		{
			if(terminal[i])
			{
				for(j=0;j<n;j++)
				{
					if(A[j]%i==0)li[k][A[j]]++,size[k]++;
				}
				k++;
			}
		}
		//printf("%d\n",k );
		// for(i=0;i<k;i++)
		// {
		// 	for(j=0;j<MAX;j++)
		// 		if(li[i][j])printf("%d ",j);
		// 	putchar(10);
		// }
		// int ans=check(0);
		// if(ans)printf("1\n");
		// else printf("0\n");
		// int ans=check(0);
		// if(ans==1)
		// {
		// 	printf("\n%d\n",n );
		// 	for(i=0;i<n;i++)printf("%d ",A[i] );
		// }
		/*memset(DP,false , sizeof DP);

		long double fact[MAX];
		fact[0]=1.00;
		for(i=0;i<MAX;i++)fact[i]=fact[i-1]*(long double)i;

		for(i=0;i<MAX;i++)		//initi
			for(j=0;j<MAX;j++)
				if(i==A[0] && j==1) DP[0][i][j]=1;
				else DP[0][i][j] = 0;

		for(i=1;i<n;i++)				//level
		{
			DP[i][A[i]][1]++;
			for(j=1;j<MAX;j++) 			//hcf
				for(k=1;k<MAX;k++)		//length
					{
						DP[i][j][k]+=DP[i-1][j][k];
						if(DP[i-1][j][k] && (j>1||k==1))
						{
							DP[i][gcd(A[i],j)][k+1]+=DP[i-1][j][k];
						}
					}
		}

		for(i=0;i<n;i++)				//level
			for(j=1;j<5;j++) 			//hcf
				for(k=1;k<5;k++)		//length
					if(DP[i][j][k])printf("level=%d hcf=%d len=%d :%lld \n", i,j,k,DP[i][j][k]);
		

		long long AR[MAX];
		memset(AR,false,sizeof AR);
		for(i=0;i<5;i++)printf("%lld ",DP[n-1][1][i]);
		*/


		// win =0.0 , loose = 0.0;
		// for(i=0;i<MAX1;i++)
		// {
		// 	if(i%10==0)random_shuffle( AR, AR+n);
		// 	myrandom();
		// }
	}
	return 0;
}