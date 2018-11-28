#include <bits/stdc++.h>
using namespace std;
int t,i,ans,p,l,cnt,h;
string s;
int main()
{
  ifstream cinf;
  ofstream coutf;
  cinf.open("input.txt");
  coutf.open("ans.txt");
    cinf>>t;
    h=1;
    while(t--)
    {
        cinf>>s;
        l=s.size();
        cnt=0;
        ans=0;
        p=0;
        for(i=l-1;i>=0;i--)
        {
            if(s[i]=='+')
            {
                cnt++;
            }
            else
            {
                s.erase(l-cnt,cnt);
                cnt=0;
                break;
            }
        }
        if(cnt>0)
        s.erase(l-cnt,cnt);
        if(s.size()>0)
        {
        for(i=0;i<(s.size()-1);i++)
        {
            if(s[i]!=s[i+1])
                ans++;
            if(s[i]=='-')
                    p=1;
        }
        if(s[s.size()-1]=='-')
            p=1;
        }
        coutf<<"Case #"<<h<<": "<<ans+p<<endl;
        h++;
    }
    return 0;
}
