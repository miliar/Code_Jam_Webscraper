#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<iostream>
#include<string.h>
#include<limits.h>
#include<functional>
#include<vector>
#include<queue>
#include<utility>
#include<stdlib.h>
#include<time.h>

typedef long long int ll;

#define VI vector<int>
#define VLL vector<ll>
#define MII map<int,int>
#define MIC map<int,char>
#define MCI map<char,int>
#define MCC map<char,char>

#define pb push_back

#define IT iterator
#define RIT reverse_iterator
#define mod 1000000007
#define mem(a) memset(a,0,sizeof(a))
using namespace std;
inline int fastRead()
      {
        int a=0;
       char c= getchar();

            while (c < '0' || c>'9') c=getchar();

            while( c >= '0' && c <= '9' )
             {
               a = (a<<3)+(a<<1) + c-'0';
               c=getchar();
             }
        return a;

      }
int main()
{
    int tc ;
    cin>>tc;
    for(int c=1;c<=tc;c++) {
        string s;
        cin>>s;
        string p = s;
        for(int i=0;i<s.length();i++) {
            if(p[0]<=s[i]) {
                p = s[i]+p;
            }
            else {
                p[i]=s[i];
            }
        }
        cout<<"Case #"<<c<<": ";
        for(int i=0;i<s.length();i++) {
            cout<<p[i];
        }
        cout<<endl;
    }
}














