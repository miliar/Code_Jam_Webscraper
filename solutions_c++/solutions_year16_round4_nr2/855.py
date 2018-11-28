#include <bits/stdc++.h>

using namespace std;

vector < double > all;
double a[55];
int i,k,n,j,t1,t;
double pr;

int main()
 {
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
  cin>>t;
  for (t1=1;t1<=t;t1++)
   {
    cout<<"Case #"<<t1<<": ";
    cin>>n>>k;
    pr=0;
    for (i=0;i<n;i++)
        cin>>a[i];
    for (int i=0;i<(1<<n);i++)
     if (__builtin_popcount(i) == k)
       {
        all.clear();
        for (int j=0;j<n;j++)
         if ((1<<j)&i) all.push_back(a[j]);
        double res=0;
        for (int j=0;j<(1<<k);j++)
         if (__builtin_popcount(j) == k/2)
           {
            double ans=1;
            for (int z=0;z<k;z++)
             if ((1<<z)&j) ans*=all[z]; else ans*=(1-all[z]);
           res+=ans;
           }
        pr=max(pr,res);
       }
    printf("%.10f\n",pr);
   }
 }
