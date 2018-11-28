#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdio.h>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <list>
#include <vector>
#include <deque>
#include <functional>

typedef long long ll;
typedef unsigned long long ull;

#define pb push_back()
#define pf push_front()
#define popb pop_back()
#define popf pop_front()
//#define rall(v) v.begin(),v.end(),greater<double>()
//#define all(v) v.begin(),v.end()
//#define SZ(x) size(x)
#define pii 2*acos(0)
#define max 4
//#define FOR(i,n) for (int i=0;i<int n ;i++)
//#define FOR1(i,n) for (int i=1;i<=int n ;i++)
//#define RF0(i,n) for (int i=(int n)-1 ;i>=0 ;i--)
using namespace std;

char chkdiag(char ch[4][4])
{   int o=0,x=0,i=0,j=0;
    char z='O';
         for (j=0;j<4;j++)
         {
          if (ch[i][j]=='O')o++;
          if (ch[i][j]=='X')x++;
          if (ch[i][j]=='T'){o++;x++;}
         i++;
         }
         if (x==4)return 'X';
         if (o==4)return 'O';
         i=0,x=0;o=0;
         for (j=3;j>=0;j--)
         {
          if (ch[i][j]=='O')o++;
          if (ch[i][j]=='X')x++;
          if (ch[i][j]=='T'){o++;x++;}
         i++;
         }
         if (x==4)return 'X';
         if (o==4)return 'O';
         return 'e';
     }

char chkhor(char ch[4][4])
{
    int i,j,k,x=0,o=0;
    for (i=0;i<4;i++)
    {
        x=0;o=0;
        for (j=0;j<4;j++)
        {
         if (ch[i][j]=='O')o++;
          if (ch[i][j]=='X')x++;
          if (ch[i][j]=='T'){o++;x++;}
        }
        if (x==4)return 'X';
         if (o==4)return 'O';

    }
    return 'e';
}

char chkver(char ch[4][4])
{
    int i,j,k,x=0,o=0,draw=0;
    for (i=0;i<4;i++)
    {
        x=0;o=0;
        for (j=0;j<4;j++)
        {
         if (ch[j][i]=='O')o++;
         if (ch[j][i]=='.')draw++;
          if (ch[j][i]=='X')x++;
          if (ch[j][i]=='T'){o++;x++;}
        }
        if (x==4)return 'X';
         if (o==4)return 'O';

    }
    if (draw!=0)return 'd';
    return 'e';
}


int main()
{
    int ptr,t,a,b,c,d,e,i,j,k,l;
    vector<double> v;
    list<double> ilist;
    deque<double> v1;

bool tf;
    char ch[max][max],chr,ans;
   // string str[max];
freopen("A-large.in","r",stdin);
    freopen("o.out","w",stdout);
    cin>>t;
     for (i=0;i<t;i++)
     {
        ans='e';
        for (j=0;j<4;j++)
        {
            cin>>ch[j];
            //cout<<"in";
            //cout<<endl<<ch[j];
        }
       ans=chkdiag(ch);
       if (ans=='X'){cout<<"Case #"<<i+1<<": "<<"X won"<<endl;continue;}
       if (ans=='O'){cout<<"Case #"<<i+1<<": "<<"O won"<<endl;continue;}
       //ans='e';
       ans=chkhor(ch);
       if (ans=='X'){cout<<"Case #"<<i+1<<": "<<"X won"<<endl;continue;}
       if (ans=='O'){cout<<"Case #"<<i+1<<": "<<"O won"<<endl;continue;}

       ans=chkver(ch);
       if (ans=='X'){cout<<"Case #"<<i+1<<": "<<"X won"<<endl;continue;}
       if (ans=='O'){cout<<"Case #"<<i+1<<": "<<"O won"<<endl;continue;}
       if (ans=='d'){cout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;continue;}
       cout<<"Case #"<<i+1<<": "<<"Draw"<<endl;
        //cout<<endl;

     }
    return 0;
}


