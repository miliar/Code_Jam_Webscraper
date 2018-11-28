#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int maxn  = 1010;
double a[maxn],b[maxn];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("ans4large.txt","w",stdout);
    int T,i,j,n,ans1,ans2;
    int ncase = 0;
    cin>>T;
    while(T--){
        ncase++;
        cin>>n;
        for(i=1;i<=n;i++) cin>>a[i];
        for(i=1;i<=n;i++) cin>>b[i];
        sort(a+1,a+1+n);
        sort(b+1,b+1+n);
        for(i=1,j=1; i<=n && j<=n; ){
            if(a[i]<b[j])   {i++;j++;}
            else j++;
        }
        ans1 = n+1-i;
       // reverse(b+1,b+1+n);
        ans2 = 0;
        for(i=1,j=1; i<=n && j<=n; ){
            if(a[i]>b[j])   {i++;j++; ans2++;}
            else i++;
        }
        //ans2 = n+1-i;
        printf("Case #%d: %d %d\n",ncase,ans2,ans1);
    }
    return 0;
}
