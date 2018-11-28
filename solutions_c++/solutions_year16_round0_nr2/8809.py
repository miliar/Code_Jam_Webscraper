#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
unordered_set<string>dp;
queue<pair<string,int> >q;
#define mp(x,y) make_pair(x,y)
int func( string s);
int check(string y);

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int p=1;
    while(t--)
    {
        string s;
        cin>>s;
        //cout<<s<<endl;
        //q.clear();
        while(!q.empty())
        {
            q.pop();
        }
        dp.clear();
        int ans=func(s);
        printf("Case #%d: %d\n",p++,ans);
    }
    return 0;
}
int check(string y)
{
    int flag=0;
      for(int i=0;i<y.size();++i)
      {
        if(y[i]=='-')
        {
           flag=1;
           break;
        }
      }
      if(flag)
      {
          return 0;
      }
      else
      {
         return 1;
      }
}
int func( string s)
{
    if(check(s))
    {
       return 0;
    }
  q.push(mp(s,0));
  dp.insert(s);

  while(!q.empty())
  {
      pair<string,int> y=q.front();q.pop();
      string si=y.first;
       //cout<<si<<" "<<y.second<<endl;
      for(int i=0;i<si.size();++i)
      {
         string z=si;
         reverse(z.begin(),z.begin()+i+1);
         for(int j=0;j<i+1;++j)
         {
                if(z[j]=='+')
                {
                    z[j]='-';
                }
                else
                {
                    z[j]='+';
                }
         }
         //cout<<"conv str = "<<z<<endl;
         //new string generated
         if(!dp.count(z))
         {
            if(check(z))
            {
               return y.second+1;
            }
            else
            {
               dp.insert(z);
              q.push(mp(z,y.second+1));
            }
         }
      }


  }

}
