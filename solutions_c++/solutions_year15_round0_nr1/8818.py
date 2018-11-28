#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#define REP(i,n) for(int i=0;i<n;++i)
#define ALL(v) v.begin(),v.end()
#define LL long long
using namespace std;

int main()
{
    int ww; cin>>ww;
    REP(t,ww)
    {
      LL result = 0;
      LL sm;cin>>sm;
      ++sm;
      string d;
      cin>>d;
      
      LL cr = 0;
      REP(i,sm)
      {
        //cout<<cr<<" "<<d[i]<<endl;
        int x = (d[i]-'0');
        if(x>0)
        {
          if(i>cr) {result+=(i-cr);cr+=(i-cr);}
          cr+=x;
        }
         // cout<<cr<<" "<<d[i]<<endl;
      }
      cout<<"Case #"<<(t+1)<<": "<<result<<endl;
     }
   return 0;
   
}
