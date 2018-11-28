#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<algorithm>
#include<utility>
#include<map>
using namespace std;
int t,n,x,ar[1005],temp[1005],ki,ka,mid,hsl,hsl2;
int maks,pos;
pair<int,int> p[1005];
map<int,int> m;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&t);
    for (int ll=1;ll<=t;ll++){
        scanf("%d",&n);
        maks=-1;
        for (int i=1;i<=n;i++){
            scanf("%d",&ar[i]);
            p[i].first=ar[i];
            p[i].second=i;
            m[ar[i]]=i;
        }

        sort(p+1,p+n+1);

        ki=1;
        ka=1;

        int ans=0;
        for (int i=1;i<=n;i++){
            //printf("%d %d\n",m[p[i].first]-ki,n-ka-m[p[i].first]+1);
            if (m[p[i].first]-ki < n-ka-m[p[i].first]+1){
                //printf("%d\n",i);
                ans+=m[p[i].first]-ki;
                for (int j=m[p[i].first];j>ki;j--){
                    swap(ar[j],ar[j-1]);
                    m[ar[j]]=j;
                }ki++;
            }else{
                ans+=n-ka-m[p[i].first]+1;
                for (int j=m[p[i].first];j<n-ka+1;j++){
                    swap(ar[j],ar[j+1]);
                    m[ar[j]]=j;
                    //printf("%d hhh\n",i);
                    //if (i==2) printf("%d\n",ar[j]);
                }ka++;
            }
            //printf("%d\n",ans);
        }

        printf("Case #%d: %d\n",ll,ans);
    }

    return 0;
}
