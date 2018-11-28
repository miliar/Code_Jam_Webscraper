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
#define max 1000
//#define FOR(i,n) for (int i=0;i<int n ;i++)
//#define FOR1(i,n) for (int i=1;i<=int n ;i++)
//#define RF0(i,n) for (int i=(int n)-1 ;i>=0 ;i--)


using namespace std;


int main()
{
    int ptr,t,a,b,c,d,e,i,j,k,l,count,key;
    vector<double> v;
    list<double> ilist;
    deque<double> v1;

int a1[4][4],a2[4][4];
    //char ch[max];
    //string str[max];
freopen("A-small-attempt0.in","r",stdin);
    freopen("o.out","w",stdout);
    cin>>t;
     for (i=0;i<t;i++)
     {
     cin>>a;
     a--;
     for (j=0;j<4;j++)
     {
         for (k=0;k<4;k++)
         {
             cin>>a1[j][k];
         }
     }
     cin>>b;
     b--;
     for (j=0;j<4;j++)
     {
         for (k=0;k<4;k++)
         {
             cin>>a2[j][k];
         }
     }
     count=0;
     for (j=0;j<4;j++)
     {
         for (k=0;k<4;k++)
         {
             if (a1[a][j]==a2[b][k])
             {count++;
             key=a2[b][k];}
         }
     }
     cout<<"Case #"<<i+1<<": ";
     if (count>=2)cout<<"Bad magician!"<<endl;
     else if (count==1)cout<<key<<endl;
     else if (count==0)cout<<"Volunteer cheated!"<<endl;

     }
    return 0;
}
