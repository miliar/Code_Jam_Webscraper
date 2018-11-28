#include<iostream>
#include<cstdio>
//#include<cstring>
//#include<algorithm>
//#include<queue>
//#include<stack>
//#include<vector>
//#include<map>


using namespace std;


int gcd(int a, int b)
{
	while((a%=b) && (b%=a));
	return a+b;
}

inline void defac(int &a, int &b)
{
	int g = gcd(a,b);
	if(g>1)
	{
		b/=g;
		a/=g;
	}
	return;
}

int main()
{
	int n;
	int a,b;	// a/b
	
	
	scanf("%d",&n);
	for(int t = 1 ; t <= n ; t++)
	{
		int ans = 0;
		
		
		scanf("%d/%d",&a,&b);
		
		defac(a,b);
		
		if((b&(-b)) != b)
		{
			printf("Case #%d: impossible\n", t);
			continue;
		}
		
		if(a >= (b>>1))
		{
			ans=1;
		}
		else
		{
			while(a < (b>>1))
			{
				b>>=1;
				ans++;
			}
			ans++;
		}
		
		
		printf("Case #%d: %d\n",t,ans);
	}
	
	return 0;
}

