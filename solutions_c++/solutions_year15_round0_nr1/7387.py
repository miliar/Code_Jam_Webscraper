#include<bits/stdc++.h>
using namespace std;
int main()
{
      freopen("example.in","r",stdin);
      freopen("outputA.out","w+",stdout);

      int T,Smax,Cnt=0,ans = 0,cass =1;
      cin>>T;
      string str;
      while(T--)
      {
            Cnt = ans =0;
            cin>>Smax;
            cin>>str;
            Cnt = (int)(str[0]-'0');
            for(int i=1; i<str.size(); i++)
            {
                  if(Cnt<i)
                  {
                        ans += (i-Cnt);
                        Cnt = i;
                  }
                  Cnt += (int) (str[i]-'0');
            }
//            cout<<ans<<endl;
            cout<<"Case #"<<cass++<<": "<<ans<<endl;
      }
      return 0;
}
