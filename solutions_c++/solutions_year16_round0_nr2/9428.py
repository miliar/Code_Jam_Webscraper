#include<bits/stdc++.h>
 using namespace std;

 const int N = 1e5 + 121;
 int a[N],b[N],kol,n,t,tt,ans,pos,i,j;
 string s;

  int main()
  {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

     //freopen("B-large.in","r",stdin);freopen("output.txt","w",stdout);

      cin>>tt;
      for(t = 1;t<=tt;++t)
      {
          cout<<"Case #"<<t<<": ";

            cin>>s;
             n = (int)s.size();
             for(i=0;i<n;++i)
              if(s[i]=='+') a[i+1]=1; else a[i+1]=0;

              b[1] = a[1];
              kol = 1;
               for(i=2;i<=n;++i)
                if(b[kol]!=a[i]) b[++kol] = a[i];
               ans = kol - 1 + (b[kol]==0);

              cout<<ans;

          cout<<endl;
      }

    return 0;
  }
