#include<stdio.h>
#include<algorithm>
using namespace std;

int n;
int a[1000]={0};
bool check[1000]={0};
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,t2;
    int i,j,mn,ans,start,end,temp;
    scanf("%d",&t2);
    for(t=1;t<=t2;t++){
        ans = 0;
        scanf("%d",&n);
        for(i=0;i<n;i++) scanf("%d",&a[i]);
        for(i=0;i<n;i++) check[i] = false;
        for(i=0;i<n;i++){
            mn = -1;
            for(j=0;j<n;j++){
                if(!check[j] && (mn==-1 || a[mn] > a[j])) mn=j;
            }
            start = end = 0;
            for(j=mn-1;j>=0;j--){
                if(!check[j]) start++;
            }
            for(j=mn+1;j<n;j++){
                if(!check[j]) end++;
            }
            if(start > end) ans += end;
            else ans += start;
            check[mn] = true;
        }
        //for(i=0;i<n;i++) printf("%d ",a[i]);
        //printf("\n");
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
