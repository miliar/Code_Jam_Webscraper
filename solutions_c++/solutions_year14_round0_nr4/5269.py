#include <iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
#define N 1005
using namespace std;
double a[N],b[N];
int match[N];
int main()
{
     freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int t,i,j,cnt,n,ics=0;
   scanf("%d",&t);
   while(t--){
        cin>>n;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        for(i=0;i<n;i++){
            cin>>b[i];
        }
        sort(a,a+n);
        sort(b,b+n);
        j=0;
        cnt=0;
        for(i=0;i<n;i++){
            while(b[j]<=a[i]&&j<n)
            j++;
            if(j==n)
            break;
            j++;
            cnt++;
        }
        int ans=0;
        j=0;
        for(i=0;i<n;i++){
            while(a[j]<=b[i]&&j<n)
            j++;
            if(j==n)
            break;
            j++;
            ans++;
        }
        printf("Case #%d: %d %d\n",++ics,ans,n-cnt);

   }
    return 0;
}
