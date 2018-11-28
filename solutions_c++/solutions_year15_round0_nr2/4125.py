#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<queue>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t,n;
    int arr[1010];
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        scanf("%d",&n);
        std::priority_queue<int> pq;
        int ans;
        int nc=0,fl=0,fl2=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
            if(arr[i]==9)
                nc++;
            else if(arr[i]>6)
                fl=1;
            else if(arr[i]>3)
                fl2++;
            pq.push(arr[i]);
        }
        if(nc==1&&fl==0&&fl2==0)
        {
            printf("Case #%d: 5\n",c);
        }
        else if(nc==1&&fl==0&&fl2==1)
        {
            printf("Case #%d: 6\n",c);
        }
        else
        {
            ans = pq.top();
            int co = 0;
            int temp;
            while(1)
            {
                temp = pq.top();
                if(temp==1)
                    break;
                ans=min(temp+co,ans);
                pq.pop();
                pq.push(temp/2);
                pq.push((temp+1)/2);
                co++;
            }
            printf("Case #%d: %d\n",c,ans);
        }
    }
    return 0;
}
