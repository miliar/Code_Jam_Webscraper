#include <bits/stdc++.h>
#define mp make_pair
#define ll long long

using namespace std;

vector <int> v;



int main()
{
   freopen( "in.txt" , "r" , stdin);
   freopen( "out.txt" , "w" , stdout);
   int t;
   cin >> t;
   int a=1;
   while(a<=t)
   {
       int l ;
       cin >> l;
       string s ;
       cin >> s;
       int y = 0 , z = 0;
       z= s[0]-'0';
       for(int i = 1 ; i < s.size() ; i++)
       {
           if(i > z && s[i] !='0')
           {
               y+= i-z;
               z+=y;
           }
           z+=s[i]-'0';
       }
       cout << "Case #" << a++ << ": " << y << endl;
   }
}



