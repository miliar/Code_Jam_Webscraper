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
    int ptr,t,a,b,c,d,e,i,j,k,l,count;
    vector<double> v;
    list<double> ilist;
    deque<double> v1;

int arr[]={1,4,9,121,484};
    //char ch[max];
    //string str[max];
freopen("C-small-attempt0.in","r",stdin);
    freopen("o.out","w",stdout);
    cin>>t;
     for (i=0;i<t;i++)
     {count=0;
     cin>>a>>b;
     for (j=0;j<5;j++)
     {
         if (arr[j]>=a&&arr[j]<=b)count++;
     }
     cout<<"Case #"<<i+1<<": "<<count<<endl;

     }
    return 0;
}
