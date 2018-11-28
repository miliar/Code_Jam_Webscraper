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
        int i,j,n,num;
        cin>>n;
        num=n;
        set<int>dig;
        cs++;
        cout<<"Case #"<<cs<<": ";
        if(n==0)
        {
                cout<<"INSOMNIA\n";
                continue;
        }
        foo(num,dig);
        while(dig.size()<10)
        {
                num+=n;
                foo(num,dig);
        }
        cout<<num<<endl;
   }
  return 0;
} 