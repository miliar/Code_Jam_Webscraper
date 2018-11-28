#include<bits/stdc++.h>
#define ll long long int
#define ld long double
#define pb(x) push_back(x)
#define put(x) printf("%d",x)
#define get(x) scanf("%lld",&x)
using namespace std;
int main()
{
  vector<ll>Aud;
  ll tst,loop=1,val,person,sum,s;
  string audience;
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  get(tst);

  while(loop<=tst)
  {
      get(s);
      sum=0;
      person=0;
      cin>>audience;
      for(int i=0;i<audience.length();i++)
      {
          Aud.pb(audience[i]-'0');
      }
      sum=Aud[0];
      for(int i=1;i<=s;i++)
      {
          if(i<=sum)
             {
                 sum+=Aud[i];
             }
             else
             {
               if(Aud[i]!=0){
                person+=(i-sum);
                sum+=Aud[i]+person;
             }
             }
      }
      printf("Case #%lld: %lld \n",loop,person);
      loop++;
  Aud.clear();
  }





return 0;
}
