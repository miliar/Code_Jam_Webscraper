#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

char n[1010];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	int T,x,peo,ans,cont=1;
	scanf("%d",&T);
	while(T--)
	{
	    peo=0;
	    ans=0;
	    scanf("%d",&x);
	    scanf("%s",n);
	    for(int i=0;i<=x;i++)
        {
            if(peo>=i) peo+=n[i]-'0';
            else
            {
                ans+=i-peo;
                peo=i+n[i]-'0';
            }
        }
        printf("Case #%d: %d\n",cont++,ans);
	}
	return 0;
}
