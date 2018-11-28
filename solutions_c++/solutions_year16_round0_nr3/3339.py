#include<bits/stdc++.h>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)
#define foreach(it, c) for (__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)

long long D;

int prime(long long x)
{
    long long i;
    if(x==1){D=1;return 0;}
    if(x==2)return 1;
    if(x%2==0){D=2;return 0;}
    for(i=3;i*i<=x && i<=30;i+=2)if(x%i==0){D=i;return 0;}
    for(i=30;i*i<=x;i+=30)
    {
        if(x%(i+1)==0){D=i+1;return 0;}
        if(x%(i+7)==0){D=i+7;return 0;}
        if(x%(i+11)==0){D=i+11;return 0;}
        if(x%(i+13)==0){D=i+13;return 0;}
        if(x%(i+17)==0){D=i+17;return 0;}
        if(x%(i+19)==0){D=i+19;return 0;}
        if(x%(i+23)==0){D=i+23;return 0;}
        if(x%(i+29)==0){D=i+29;return 0;}
    }
    return 1;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T, t = 0;
	scanf("%d", &T);
	while(T--)
	{
		t++;
		printf("Case #%d:\n", t);
		long long N, J, ans[12], NUM[12];
		scanf("%lld %lld", &N, &J);
		
		for(int i=(1<<15)+1; J && i < (1<<16); i+=2)
		{
			bool flag = 1;
			for(int j=2; j<=10; j++)
			{
				long long num = 0, m = 1;
				for(int k=0; k<16; k++)
					num += (bool)(i&(1<<k)) * m, m *= j;
				if(prime(num))
				{
					flag = 0;
					break;
				}
				ans[j] = D;
				NUM[j] = num;
			}
			if(flag)
			{
				for(int k=15; k>=0; k--)
					printf("%d", (bool)(i&(1<<k)));
				for(int k=2; k<=10; k++)
					printf(" %d", ans[k], NUM[k]);
				printf("\n");
				J--;
			}
		}
	}
}






