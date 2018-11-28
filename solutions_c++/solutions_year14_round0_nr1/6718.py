#include<iostream>
#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<map>
#include<math.h>
#include<climits>
#include<time.h>
using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output1.txt","w",stdout);
    #endif
    //clock_t start=clock();
    int t;
    scanf("%d",&t);
    for(int cas=1; cas<=t; cas++)
    {
        int arr[20]={0}, arr2[20]={0}, a, b, ans, ar[6][6], co=0;
        scanf("%d",&a);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                scanf("%d",&ar[i][j]);
        for(int j=1; j<=4; j++)
            arr[ar[a][j]]=1;
        scanf("%d",&a);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                scanf("%d",&ar[i][j]);
        for(int j=1; j<=4; j++)
            arr2[ar[a][j]]=1;
        for(int i=0; i<20; i++)
            arr[i]&=arr2[i];
        for(int i=0; i<20; i++)
        {
            if(arr[i])
            {
                co++;
                ans=i;
            }
        }
        if(co==0)
            printf("Case #%d: Volunteer cheated!\n", cas);
        else if(co==1)
            printf("Case #%d: %d\n", cas, ans);
        else
            printf("Case #%d: Bad magician!\n", cas);
    }

    //while (clock() - start < (0.98) * CLOCKS_PER_SEC);
    return 0;
}
