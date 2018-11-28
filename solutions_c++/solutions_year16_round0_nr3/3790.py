#include<bits/stdc++.h>
 
using namespace std;
 
#define rep(i,n) for(i=0;i<n;i++)
#define elif else if
#define pii pair<int,int>
#define pb push_back
#define gc getchar_unlocked
#define mp make_pair
#define ll long long
 
int N=16;
void fit(int n, vector<int>&num)
{
        int i;
        for(i=1;i<N-1;i++)
        {
                if(n==0)
                    break;
                num[i]=n%2;
                n/=2;
        }
        return;
}
ll int div(ll int val)
{
        ll int i,lim;
        for(i=2;i*i<=val;i++)
        {
                if(val%i==0)
                        return i;
        }
        return -1;
}
vector<int> check( vector<int> num)
{
        int base=2,i;
        ll int val,pp;
        vector<int>ans;
        for(base=2;base<=10;base++)
        {
                val=0;
                pp=1;
                for(i=0;i<N;i++)
                {
                        if(num[i]==1)
                                val+=pp;
                        pp*=base;
                }
                int fac= div(val);
                if(fac==-1)
                        return ans;
                ans.pb(fac);
        }
        return ans;
}
int main()
{
   freopen("inp.in","r",stdin);
   freopen("aout.txt","w",stdout);
   int t,cs=0;
   cin>>t;

   while(t--)
   {
        int n,j,i,lim;
        cs++;
        cin>>n>>j;
        N=n;
        vector<int>num(n,0);
        num[0]=num[n-1]=1;
        lim=pow(2,n-2);
        cout<<"Case #"<<cs<<": ";
        for(i=0;i<lim;i++)
        {
                fit(i,num);
                vector<int> fac= check(num);
                if(fac.size()==9)
                 {
                        j--;
                        cout<<"\n";
                        for( int k=n-1;k>=0;k--)
                                cout<<num[k];
                        for(int k=0;k<9;k++)
                                cout<<" "<<fac[k];
                  }      
                if(!j)
                break;
        }
   }
  return 0;
} 