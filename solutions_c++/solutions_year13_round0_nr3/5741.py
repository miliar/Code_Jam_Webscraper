#include<cstdio>
#include<algorithm>
using namespace std;

int arr[]={1,4,9,121,484};

int main()
{
    int t,a,b,ans;
    scanf("%d",&t);
    for(int caseno=1;caseno<=t;caseno++)
    {
        ans=0;
        scanf("%d %d",&a,&b);
        for(int i=0;i<6;i++)
        {
            if(arr[i]<=b && arr[i]>=a) ans++;
        }
        printf("Case #%d: %d\n",caseno,ans);
    }
    return 0;
}
