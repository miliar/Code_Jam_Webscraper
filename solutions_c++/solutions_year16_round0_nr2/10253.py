#include<bits/stdc++.h>
using namespace std;
int main()
{
//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
  int t;
  cin>>t;
  for(int i=1;i<=t;i++)
{
    string s;
    cin>>s;
    int c = 0,k = s.length()-1;

    while(s[k] == '+')
        s.erase(s.begin()+(k--));
    k = s.length();
    string ss="";

    for(int j = 0; j < k; j++)
        ss += '+';
    while(s != ss)
    {
        int z = 0;
        if(s[z] == '-')
        {
            while(s[z] == '-')
                s[z++] = '+';

        }
        else
        {
            while(s[z] == '+')
                s[z++] = '-';
        }

        c++;
    }
    cout<<"Case #"<<i<<": "<<c<<endl;
}

  return 0;
}
