#include<bits/stdc++.h>
 
using namespace std;
 
#define rep(i,n) for(i=0;i<n;i++)
#define elif else if
#define pii pair<int,int>
#define pb push_back
#define gc getchar_unlocked
#define mp make_pair
#define ll long long
 
void foo( int num,set<int>&v)
{
        while(num>0)
        {
                int dig=num%10;
                v.insert(dig);
                num/=10;
        }
        return;
}
int main()
{
   freopen("inp.in","r",stdin);
   freopen("aout.txt","w",stdout);
   int t,cs=0;
   cin>>t;
   while(t--)
   {
        int i,j,ans=0,num;
        string s;
        cin>>s;
        num=0;
        cs++;
        int l=s.size();
        for(i=l-1;i>=0;i--)
        {
                int now;
                if(s[i]=='+')
                        now=0;
                else
                        now=1;
                if( (now+num)%2 )
                {
                        ans++;
                        num++;
                }
        }
        cout<<"Case #"<<cs<<": "<<ans<<endl;
   }
  return 0;
} 