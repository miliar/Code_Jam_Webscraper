/*
By Tianyi Chen. All rights reserved.
Date: 2016-04-09
*/
#include<bits/stdc++.h>
using namespace std;
long long m,n;
int __=1000000,ans;bool existed[10];
int main() {
 infile("D:/publish/GCJ/2016-Qualification/A.in");
 outfile("D:/publish/GCJ/2016-Qualification/A.out");
 scanf("%d",&__);
 for(int _=1;_<=__;++_) {
  memset(existed,0,sizeof existed);m=0;ans=-1;
  scanf("%lld",&n);
  if (!n) { printf("Case #%d: INSOMNIA\n",_); continue; }
  for (int j=0;;++j) {
   m+=n;
   auto s=to_string(m);
   for (auto&&x:s)existed[x-'0']=1;
   if (count(existed,existed+10,true)==10) {
    ans=1;break;
   }
  }
  if (~ans)printf("Case #%d: %d\n",_,m);else printf("Case #%d: INSOMNIA\n",_);
 }
}