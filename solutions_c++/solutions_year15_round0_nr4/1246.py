#include <bits/stdc++.h>
#define mp make_pair
#define ll long long

using namespace std;

char v [10005];
bool bol [10005];
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
       int x , r , c;
       cin >> x >> r >> c;
       cout << "Case #" << a++ << ": " ;
       if(x==1)
        cout << "GABRIEL" << endl;
       else if(x==2)
       {
           if((r*c)%2==0)
           {
               cout << "GABRIEL" <<endl;
           }
           else
           {
               cout << "RICHARD" << endl;
           }
       }
       else if(x==3)
       {
           if(c==r && c==3 )
           {
               cout << "GABRIEL" << endl;
           }
           else if(r==4 && c==3 )
           {
               cout << "GABRIEL" << endl;
           }
           else if(r==3 && c==4 )
           {
               cout << "GABRIEL" << endl;
           }
           else if(r==2 && c==3)
           {
               cout << "GABRIEL" << endl;
           }
           else if(c==2 && r==3)
           {
               cout << "GABRIEL" << endl;
           }
           else
           {
               cout << "RICHARD" << endl;
           }
       }
       else
       {
           if(c==3 && r==4)
           {
                cout << "GABRIEL" << endl;
           }
           else if(c==4 && r==3)
           {
               cout << "GABRIEL" << endl;
           }
           else if(c==r && c==4)
           {
               cout << "GABRIEL" << endl;
           }
           else
           {
               cout << "RICHARD" << endl;
           }
       }
   }
}



