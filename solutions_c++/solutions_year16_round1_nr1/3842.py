#include<bits/stdc++.h>
#define lli long long int
#define pb push_back
#define mod 1000000007
#define pii pair<int,int>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,n,k,l,tr=0;
    string s;
    char a[2005];
    cin>>t;
    while(t--)
      {
         tr++;
         cin>>s;
         k=1000;l=1000;
         a[1000]=s[0];
         for(i=1;i<s.size();i++)
          {
            if(s[i]>=a[k])
                {
                    a[k-1]=s[i];
                      k--;
                }
               else
                { a[l+1]=s[i];
                 l++; }
             }
             cout<<"Case #"<<tr<<": ";
        for(i=k;i<=l;i++)
           cout<<a[i];
           cout<<endl;
      }
    return 0;
    }
