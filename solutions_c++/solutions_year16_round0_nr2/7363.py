#include <bits/stdc++.h>

using namespace std;

int revers (string s)
{
   int ans=0;
   bool b=true;
   for (int i=0; i<s.length(); i++)
   {
       if (s[i]=='-') b=false;
   }
   while (!b)
   {
       int cur_pos=s.length()-1;
       while (s[cur_pos]!='-')
       {
           cur_pos--;
       }
       for (int i=0; i<=cur_pos; i++)
       {
           if (s[i]=='+') s[i]='-';
           else if (s[i]=='-') s[i]='+';
       }
       ans++;
       b=true;
       for (int i=0; i<s.length(); i++)
       {
           if (s[i]=='-') b=false;
       }
   }
   return ans;
}

int main()
{
    freopen ("B-large.in", "r", stdin);
    freopen ("output.in", "w", stdout);
    int t;
    cin>>t;
    vector <int> otv(t);
    for (int i=0; i<t; i++)
    {
        string s;
        cin>>s;
        otv[i]=revers(s);
    }
    for (int i=0; i<t; i++)
    {
        cout<<"Case #"<<i+1<<": "<<otv[i]<<endl;
    }
    return 0;
}
