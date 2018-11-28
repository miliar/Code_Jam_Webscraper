#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define maxn 1010
using namespace std;
double a[maxn],b[maxn];
int main (){
    int t,n;
    //freopen("D-large.in","r",stdin);
    //freopen("D-large.out","w",stdout);
    scanf("%d",&t);
    for(int Case=1;Case<=t;++Case){
        scanf("%d",&n);
        for(int i=0;i<n;++i)scanf("%lf",&a[i]);
        for(int i=0;i<n;++i)scanf("%lf",&b[i]);
        sort(a,a+n);sort(b,b+n);
        //for(int i=0;i<n;++i)cout<<a[i]<<" ";
        //cout<<endl;
        //for(int i=0;i<n;++i)cout<<b[i]<<" ";
        //cout<<endl;
        int ans=0;
        int temp=0;
        for(int i=0;i<n;++i){
            while(temp<n&&b[temp]<a[i])temp++;
            if(temp>=n){
                ans=n-i;
                break;
            }
            temp++;
        }
        int ans2=0;
        int j=0;
        for(int i=0;i<n;++i){
            if(a[i]<b[j]){
            }
            else{
                ans2++;
                j++;
            }
        }
        printf("Case #%d: %d %d\n",Case,ans2,ans);
    }
}
