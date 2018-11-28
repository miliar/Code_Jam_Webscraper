#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{

    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int tc, fg, sg, temp, ans;
    vector<int>f;
    vector<int>s;
    cin>>tc;
    for(int t=1; t<=tc; t++)
    {
        cin>>fg;
        f.clear();
        s.clear();
        for(int i=1; i<=4; i++)
        {

            for(int j=1; j<=4; j++)
            {
                cin>>temp;
                if(i==fg)
                   f.push_back(temp);
            }
        }
        cin>>sg;
         for(int i=1; i<=4; i++)
        {

            for(int j=1; j<=4; j++)
            {
                cin>>temp;
                if(i==sg)
                    s.push_back(temp);
            }
        }
      int counter = 0;
      for(int i=0; i<4; i++)
      {
          for(int j=0; j<4; j++)
          {
                if(f[i]==s[j])
                {
                    ans = f[i];
                    counter++;
                }
          }

      }

      cout<<"Case #"<<t<<": ";
      if(counter==0)
        cout<<"Volunteer cheated!"<<endl;
      else if(counter==1)
        cout<<ans<<endl;
      else
        cout<<"Bad magician!"<<endl;
    }
}
