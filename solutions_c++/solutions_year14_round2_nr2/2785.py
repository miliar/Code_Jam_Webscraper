using namespace std;
#include<iostream>

int n,m,k,c,d,vol,t;
int a , b ;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int test;
    scanf("%d",&test);
    int p;
    p=1;
    while(test--) 
	{
		int a,b,k;
		int i,j;
        int cnt =0;
        scanf("%d %d %d",&a,&b,&k);
        for(i=0;i<a;i++) 
		{
            for(j=0;j<b;j++) 
			{
                if ((i&j)<k) 
                    cnt++;
            }
        }
        printf("Case #%d: %d\n",p++,cnt);
    }
    return 0;
}
