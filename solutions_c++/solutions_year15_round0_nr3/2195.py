#include <bits/stdc++.h>
#define mp make_pair
#define ll long long

using namespace std;

char v [10005];
bool bol [10005];
string l;
int x;
bool getb(char a , char b )
{
    if(a==b )
        return false;
    if(a=='j' && b=='i')
        return false;
    if(a=='k' && b=='j')
        return false;
    if(a=='i' && b=='k')
        return false;
    return true;
}
char getbb(char a , char b)
{
    if(a==b )
        return '1';
    if(a=='j' && b=='i' || a=='i' && b=='j')
        return 'k';
    if(a=='k' && b=='j' || a=='j' && b=='k')
        return 'i';
    if(a=='i' && b=='k' || a=='k' && b=='i')
        return 'j';
    if(a=='1')
        return b;
    if(b=='1')
        return a;
}

int main()
{
   freopen( "in.txt" , "r" , stdin);
   freopen( "out.txt" , "w" , stdout);
   int t;
   cin >> t;
   int a=1;
   while(a<=t)
   {
       int z;
       cin >> z >> x;
       cin >> l;
       char b ='1';
       string ans ="l";
       bool flag = true;
       string s ;
       for(int i = 0 ; i < x ; i++)
        s+=l;
       cout << "Case #" << a++ << ": ";
       for(int i = 0 ; i < s.length() ; i++)
       {
           flag = ((flag && getb(b , s[i])) || (flag==false && getb(b,s[i])==false));
           b=getbb(b,s[i]);
           v[i]=b;
           bol[i]=flag;
       }
       if(flag || b!='1')
       {
           cout << "NO" << endl;
       }
       else
       {
           bool ff = false;
           for(int i = 0 ; i < s.size() ; i++)
           {
               if(v[i]=='i' && bol[i])
               {
                   bool f =false;
                   for(int j = i+1 ; j < s.size() ;j++)
                   {
                       if(v[j]=='k' && bol[j])
                       {
                           f=true;
                           break;
                       }
                   }
                   if(f)
                   {
                       ff=true;
                       break;
                   }
               }
           }
           if(ff)
           {
               cout << "YES" << endl;
           }
           else
            cout << "NO" << endl;
       }
   }
}



