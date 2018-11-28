#include <bits/stdc++.h>
using namespace std;
int maxWord, n;


int main()
{

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);


    int i,j,kase=1,t,msk,k,sn,nw;
    string s;
    scanf("%d",&t);
    long long int ans;
    while(t--)
    {
        cin>>s;
        n=s.size();
        s+='+';
        if(s[0]=='-') sn=0;
        else sn=1;

        ans=0;

        for(i=0;i<n;i++)
            {
              if(s[i]!=s[i+1])
              {
                  ans++;
                  for(j=0;j<=i;j++)
                    s[j]=s[i+1];
              }
            }
        printf("Case #%d: %lld\n",kase++,ans);
    }
    return 0;
}

