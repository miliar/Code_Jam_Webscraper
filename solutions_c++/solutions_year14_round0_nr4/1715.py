#include<iostream>
#include<cstdio>
#include<queue>
#include<algorithm>
using namespace std;

const int maxn = 1505;
int n;
double a[ maxn ],b[ maxn ];
bool vis[ maxn ];
//int ans;

void init()
{
	int i;
	for (i=0;i<n;i++) scanf("%lf",a+i);
	for (i=0;i<n;i++) scanf("%lf",b+i);
}

int solve1()
{
	sort(a,a+n);
	sort(b,b+n);

	int worse,best,i,p;
	queue<double>pj;

	int ans = 0;
	worse=0;best=n-1;
	ans=0;
	
	for (i=n-1;i>=0;i--)
	{
		if(b[i]>a[best])
		{
			if (!pj.empty())
			{
				 p=pj.front();
				 pj.pop();
				 
				 if (p==b[i])
				 {
				    //ans-=1;
					pj.push(p);
				 }
				 worse++;
			}
			else
			{
   				//ans-=1;
				worse++;
			}
		}
		else
		if (b[i]<a[best])
		{
			ans+=1;
			best--;
		}
		else
		{
		    if (!pj.empty())
			{
				 p=pj.front();
				 pj.pop();
				 
				 if (p!=b[i])  worse++; 
				 else
				 {
				 	pj.push(p);
				 	pj.push(a[best]);
				  	best--;
				 }
			}
			else
			{
			  	pj.push(a[best]);
 	        	best--;
			}
		}
	}
	return ans;
}

int solve2()
{
	int ans = 0;
	memset( vis,false,sizeof( vis ) );
	/*sort( b,b+n );
	for( int i=0;i<n;i++ ){
		printf("%.3lf ",a[i]);
	}
	printf("\n");
	for( int i=0;i<n;i++ ){
		printf("%.3lf ",b[i]);
	}*/
	printf("\n");
	for( int i=0;i<n;i++ ){
		int ind = -1;
		double mn = 10000.0;//the min
		for( int j=n-1;j>=0;j-- ){
			if( !vis[j] ){
				if( b[j]>a[i] ){
					if( b[j]<mn ){
						mn = b[j];
						ind = j;
					}
				}
				else break;
			}
		}
		if( ind!=-1 ){
			vis[ ind ] = true;
			//printf("ind = %d\n",ind);
		}
		else{
			for( int j=0;j<n;j++ ){
				if( !vis[j] ){
					vis[ j ] = true;
					//printf("ans++ j = %d\n",j);
					break;
				}
			}
			ans ++;
		}
	}
	return ans;
}

int main()
{//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T;
	int ca = 1;
	scanf("%d",&T);
	while( T-- )
	{
		scanf("%d",&n);
		init();
		int ans1 = solve1();
		//printf("%d\n",ans);
		int ans2 = solve2();
		printf("Case #%d: ",ca++);
		printf("%d %d\n",ans1,ans2);
	}
	return 0;
}