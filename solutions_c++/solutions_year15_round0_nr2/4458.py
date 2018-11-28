#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<map>
#include<set>
#include<vector>
#include<string>
#include<queue>
#include<algorithm>
#define mod 10000007
#define INF 89999999999999LL
#define MAXN 1010
#define ll __int64
using namespace std;
int a[1200];
int main(){
	//freopen("C:\\Users\\user\\Desktop\\in.txt","r",stdin);
	//freopen("C:\\Users\\user\\Desktop\\out.txt","w",stdout);
    int t,step=0;
    int n,i,j,max1,min1,sum;
    scanf("%d",&t);
    while(t--)
	{
        scanf("%d",&n);
        for(i=0;i<n;i++)
		{
            scanf("%d",&a[i]);
            max1=max(max1,a[i]);
		}
        min1=max1;
        for(i=1;i<=max1;i++)
		{
            sum=i;
            for(j=0;j<n;j++)
			{
                if( a[j]>i )
				{
                    if( a[j]%i == 0 )
                        sum+=(a[j]/i-1);
                    else
                        sum+=(a[j]/i) ;
                }
            }
            min1=min(min1,sum);
        }
        printf("Case #%d: %d\n",++step,min1);
    }
    return 0 ;
}


