#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
char str[3000];
int main()
{
    ll t,n,i,ans[3000],k;
    ios::sync_with_stdio(false);
    //freopen("input.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>t;
    ll r=1,p;
    int a[26];
    while(r<=t)
    {
          k=0;
          memset(a,0,sizeof(a));
          memset(ans,0,sizeof(ans));
          cin>>str;
          n=strlen(str);
          for(i=0;i<n;i++)
          a[str[i]-'A']++;
          p=0;
          while(a[25]>0 && p<=n)
          {
              ans[k]=0;
              k++;
              a['Z'-'A']--;
              a['E'-'A']--;
              a['R'-'A']--;
              a['O'-'A']--;
              p+=4;
          }
          while(a['X'-'A']>0 && p<=n)
          {
              ans[k]=6;
              k++;
              a['S'-'A']--;
              a['I'-'A']--;
              a['X'-'A']--;
              p+=3;
          }
           while(a['G'-'A']>0 && p<=n)
          {
              ans[k]=8;
              k++;
              a['E'-'A']--;
              a['I'-'A']--;
              a['G'-'A']--;
              a['H'-'A']--;
              a['T'-'A']--;
              p+=5;
          }
           while(a['U'-'A']>0 && p<=n)
          {
              ans[k]=4;
              k++;
              a['F'-'A']--;
              a['O'-'A']--;
              a['U'-'A']--;
              a['R'-'A']--;
              p+=4;
          }
           while(a['W'-'A']>0 && p<=n)
          {
              ans[k]=2;
              k++;
              a['T'-'A']--;
              a['W'-'A']--;
              a['O'-'A']--;
              p+=3;
          }
           while(a['T'-'A']>0 && p<=n)
          {
              ans[k]=3;
              k++;
              a['T'-'A']--;
              a['H'-'A']--;
              a['R'-'A']--;
              a['E'-'A']--;
              a['E'-'A']--;
              p+=5;
          }
           while(a['S'-'A']>0 && p<=n)
          {
              ans[k]=7;
              k++;
              a['S'-'A']--;
              a['E'-'A']--;
              a['V'-'A']--;
              a['E'-'A']--;
              a['N'-'A']--;
              p+=5;
          }
           while(a['F'-'A']>0 && p<=n)
          {
              ans[k]=5;
              k++;
              a['F'-'A']--;
              a['I'-'A']--;
              a['V'-'A']--;
              a['E'-'A']--;

              p+=4;
          }
           while(a['O'-'A']>0 && p<=n)
          {
              ans[k]=1;
              k++;
              a['O'-'A']--;
              a['N'-'A']--;
              a['E'-'A']--;
              p+=3;
          }
           while(a['N'-'A']>0 && p<=n)
          {
              ans[k]=9;
              k++;
              a['N'-'A']--;
              a['I'-'A']--;
              a['N'-'A']--;
              a['E'-'A']--;
              p+=4;
          }
          cout<<"Case #"<<r<<": ";
          sort(ans,ans+k);
          for(i=0;i<k;i++)
          cout<<ans[i];
          cout<<endl;
          r++;
        }


    }

