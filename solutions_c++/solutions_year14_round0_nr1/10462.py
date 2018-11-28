#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<map>
#include<math.h>
#include<climits>

using namespace std;

int arr[5][5], arr2[5][5];

int main()
{
    freopen("magictrick.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n,n2,cnt=1;
    scanf("%d", &t);
    while(t--)
    {
        int flag=0, magic;
        scanf("%d", &n);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                scanf("%d", &arr[i][j]);
        scanf("%d", &n2);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                scanf("%d", &arr2[i][j]);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                if(arr[n][i]==arr2[n2][j])
                {
                    flag++;
                    magic=arr[n][i];
                }

        if(flag==1)
            printf("Case #%d: %d\n", cnt++, magic);
        else if(flag==0)
            printf("Case #%d: Volunteer cheated!\n", cnt++);
        else if(flag>1)
            printf("Case #%d: Bad magician!\n", cnt++);
    }
    return 0;
}
