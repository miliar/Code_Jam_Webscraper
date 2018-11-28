#include <cmath>
#include <cstdio>
#include <map>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <stack>
using namespace std;
#define REP(I,N)   FOR(I,0,N)
#define pb push_back
#define LL long long
#define ff first
#define ss second
int main()
{
   freopen("inp.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    int tcase;
    cin>>tcase;
    for(int tc=1; tc<=tcase; tc++)
    {
        string s;
        cin>>s;
        int k;
        cin>>k;
        int d=0;
        int i=0,j=s.size()-1;
        while(i<j)
        {
           if(s[i]=='-')
           {
               int p=k;
               for(int l=i;l<s.size() && p;l++,p--)
               {
                   if(s[l]=='-')
                    s[l]='+';
                   else
                    s[l]='-';
               }
               d++;
           }
           if(s[j]=='-')
           {
               int p=k;
               for(int l=j;l>=0 && p;l--,p--)
               {
                   if(s[l]=='-')
                    s[l]='+';
                   else
                    s[l]='-';
               }
               d++;
           }
           i++;
           j--;
        }
        int f=1;
        for(char c:s)
            if(c=='-')
            f=0;
        if(f)
        cout<<"Case #"<<tc<<": "<<d<<endl;
        else
         cout<<"Case #"<<tc<<": IMPOSSIBLE"<<endl;

    }
    return 0;
}


