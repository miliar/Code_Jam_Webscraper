#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define FOR(x,t) for(int x=0;x<t;x++)
#define read(tag)  freopen(tag,"r",stdin)
#define rite(tag) freopen(tag,"w",stdout)
#define all(typ)    typ.begin(),typ.end()
#define print(ns) cout<<"Case #"<<i<<": "<<ns<<"\n"
#define lower_all(STR) transform(STR.begin(),STR.end(),STR.begin(),::tolower)
#define LL long long
using namespace std;

int main()
{
   read("in.txt"); rite("out.txt");
   int T,n,total,ans;cin>>T;
   vector<int>arr;
   for(int i=1;i<=T;i++)
   {
      cin>>n;
      arr.clear(); arr.resize(n+1);
      total=0; ans=0;
      for(int j=0;j<=n;j++) scanf("%1d",&arr[j]);
      total=arr[0];
      for(int k=1;k<=n;k++)
      {
         if(total<k) { ans++; total++;}
         total+=arr[k];
      }
      print(ans);
   }
   return 0;
}