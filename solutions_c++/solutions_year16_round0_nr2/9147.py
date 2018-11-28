#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
      freopen("aaainput.txt","r",stdin);
      freopen("aaaoutput.txt","w",stdout);

    int test;
    cin >> test;
    for(int i=1;i<=test;i++)
    {
       string s;
       cin >> s;
       int sz=s.size();
       int counter=1;
       char x=s[0];
       for(int k=1;k<sz;k++)
       {
         if(s[k]!=x)
         {
             counter++;
             x=s[k];
         }

       }
       if(s[sz-1]=='+')
            cout << "Case #" << i << ": " << counter-1 << endl;
       else
            cout << "Case #" << i << ": " << counter << endl;



    }

    return 0;
}
