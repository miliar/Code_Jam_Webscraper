#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define INF 0x3f3f3f3f
typedef long long LL;
int A[12];
bool check()
{
	for(int i=0;i<10;i++)
	if(A[i]==0) return false;
	return true;
}

int main()
{
//    freopen("A-large.in","r",stdin);
  //  freopen("A-small-attempt4.out","w",stdout);
	int i,j,k;
	int t;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		memset(A,0,sizeof A);
		int n,m;
		int a;
		n=0;
		scanf("%d",&a);
		printf("Case #%d: ",i);
//		cout<<a<<" ";
		for(j=1;j<=1000;j++)
        {
            n+=a;
            m=n;
            while(m)
            {
                A[m%10]=1;
                m/=10;
            }
            if(check())
            {
                printf("%d\n",n);
                break;
            }
        }
        if(!check())
        {
            printf("INSOMNIA\n");
        }

	}
	return 0;
}

