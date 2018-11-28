#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<vector>
#include<queue>
#include<map>
using namespace std;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("Cout.txt","w",stdout);
    int T,A,B;
    int arr[]={1,4,9,121,484};
    scanf("%d",&T);
    int res=0;
    for(int t=1;t<=T;t++)
    {
        res=0;
        scanf("%d%d",&A,&B);
        for(int i=0;i<5;i++)
            if(arr[i]>=A && arr[i]<=B)
                res++;
        printf("Case #%d: %d\n",t,res);
    }
}
