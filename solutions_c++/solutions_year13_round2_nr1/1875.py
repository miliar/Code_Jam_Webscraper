#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<math.h>
using namespace std;
int main()
{
    int t,n,a,arr[110],i,j,k,done,left,ans,sum[110];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        memset(sum,0,sizeof(sum));
        scanf("%d %d",&a,&n);
        for(j=0;j<n;j++)
        {
            scanf("%d",&arr[j]);
        }
        sort(arr,arr+n);
        done=0;
        left=n;
        j=0;
        ans=0;
        while(done<n)
        {
//		printf("%d ",a);
            if(a>arr[j]){
                sum[j]=0;
                a+=arr[j];
                j++;
                done++;
                left--;
//                printf("condition1 ");
            }
            else
            {
//                printf("%d %d",arr[j],a);
		
		    k=0;
                if(a==1)
			k=left;
		else
		{
			while(arr[j]>=a)
			{
				a+=(a-1);
				k++;
			}

		}
                if(k<left)
                {
                    done++;
                    left--;
                    sum[j]=k;
                    a+=arr[j];
                    j++;
    //                printf("condition 3 %d ",k);
                    ans+=k;
                }
                else
                {
      //              printf("condition4 ");
                    sum[j]=left;
                    done=n;
                    ans+=left;
                    left=0;
                }
            }
        }
        for(j=n-2;j>=0;j--)
        {
            sum[j]+=sum[j+1];
            if(sum[j]>(n-j))
                sum[j]=n-j;
        }
        printf("Case #%d: %d\n",i,sum[0]);
    }
    return 0;
}
