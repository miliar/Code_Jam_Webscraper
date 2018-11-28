#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt", "rt", stdin);
   freopen("out.txt", "wt", stdout);

   int T , z = 0;
   cin >> T ;
   while(T--)
   {
       string s , t ="" ;
       cin >> s ;

       t += s[0] ;

       for(int i=1 ; i<s.size() ; i++)
       {
           if( s[i] >= t[0] )
                t = s[i] + t ;
           else
                t += s[i] ;
       }

       cout << "Case #" << ++z << ": " << t << "\n";

   }
}
