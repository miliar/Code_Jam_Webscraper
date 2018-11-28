#include <bits/stdc++.h>
/*#include <boost/multiprecision/cpp_int.hpp> */
#define ll long long
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define gc getchar_unlocked
#define pp pair<int,int>
#define bigint boost::multiprecision::cpp_int
#define bsize 600
#define ms multiset<int,greater<int> >
using namespace std;

map<ms,int> dp;
int solve(multiset<int,greater<int> > s)
{
    if(*s.begin()==1)return 1;
  if(dp.count(s))return dp[s];
   int val=*s.begin();
   multiset<int,greater<int> > temp;
   for(multiset<int,greater<int> >::iterator it=s.begin();it!=s.end();++it)
   {
       if(*it>1)temp.insert(*it -1);
   }
   s.erase(s.find(val));
   int ret=solve(temp)+1;
   for(int z=1;z<=(val+1)/2;z++)
   {

   s.insert(z);
   s.insert(val-z);
   ret=min(ret,1+solve(s));
   s.erase(s.find(z));
   s.erase(s.find(val-z));
   }

s.insert(val);

   return dp[s]=ret;
}

int t,d,ans;
multiset<int,greater<int> > ss;
int main()
{
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>d;
        ss.clear();
        int val;
        //if(i==31)cout<<d<<" ";
        while(d--){cin>>val;  ss.insert(val);}//if(i==31)cout<<val<<" ";

        cout<<"Case #"<<i<<": "<<solve(ss)<<"\n";

    }
return 0;
}

