#include<bits/stdc++.h>
using namespace std;
int rec(int r,int w)
{
    if(r>w)
        return min(1+rec(r-w,w),1+rec(r-1,w));
    else if(r<=w)
        return w;
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("out","w",stdout);
   int t;
   scanf("%d",&t);
   int l,r,w;
   for(int ii=1;ii<=t;ii++)
   {
       scanf("%d %d %d",&l,&r,&w);
      //cout<<rec(r,w)<<endl;
       printf("Case #%d: %d\n",ii,rec(r,w));
   }
    return 0;
}
