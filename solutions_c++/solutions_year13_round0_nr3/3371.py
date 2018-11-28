#include<cstdio>
#include<set>
#include<cstring>
#include<algorithm>
#include<queue>
#include<cmath>
#include<iostream>
#include<vector>
using namespace std;
typedef long long LL;
typedef pair<int,int> pi;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<pi> vpii;
#define pb push_back
#define nd second
#define st first
#define mp make_pair
#define rep(i,n) for(int i=0;i<n;i++)
#define inf 9999999999
#define MAX 1000000

      
int n,m,k,l,cas=1,t; 
int ans;
LL a, b ,act;
void read()
{
   cin>>a>>b;
}      
//No need reverse (if it is Palindrome)
vector <int> itv(LL num)
{
       vi v;
       while(num!=0)
       {
                    v.pb(num%10);
                    num/=10;             
       }
       return v;
}  

bool isPalindrome(vector<int> x)
{
     for(int i=0; i<x.size();i++)
     {
          if(x[i]!=x[x.size()-i-1]) return false;   
     }
    return true; 
}     
      
void solve()
{
     act= (LL) sqrt(a);
     
     while(true)
     { // cout<<act<<" "<<act*act<<"\n";
          if(act*act<a) act++;
         if(act*act > b) break;
         if(isPalindrome(itv(act)) && 
         isPalindrome(itv( (act*act)))){
                  // cout<<act<<"j "<<act*act<<"\n";        
                           ans++;
         }
         act++;       
      }
     
     cout<<"Case #"<<cas<<": "<<ans<<"\n";
}

int main()
{
        cin>>t;
        
          rep(ii,t)
          {
              read();
              ans=0;
               solve();
               cas++;
         }
                   
     
          return 0;
}
