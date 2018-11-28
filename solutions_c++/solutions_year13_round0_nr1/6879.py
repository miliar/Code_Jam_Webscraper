#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<bitset>
#include<list>
#include<iomanip>
#include<string>
#include<climits>
#include <sstream>
#include <fstream>
#include<cctype>
#include<time.h>
#include<assert.h>
#include <numeric>
#include <functional>
#include<cstring>
#include<cmath>
#include<iterator>
#include <memory.h>
#include<utility>
#include <ctime>
#include<algorithm>
#define all(v) v.begin(),v.end()
#define read(a) freopen("a.txt","r",stdin)
#define write(b) freopen("b.txt","w",stdout)
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define min4(a,b,c,d) min(min(a,b),min(c,d))
#define max4(a,b,c,d) max(max(a,b),max(c,d))
#define maxall(v) *max_element(all(v))
#define minall(v) *min_element(all(v))
#define pb push_back
#define mk make_pair
#define SORT(v) sort(all(v))
#define UN(v) SORT(v), (v).earse(unique(all(v)),v.end())
#define common(a,b) SORT(a), SORT(b), a.erase(set_intersection(all(a),all(b),a.begin()),a.end())
#define uncommon(a,b) SORT(a), SORT(b), a.erase(set_symmetric_difference(all(a),all(b),a.begin()),a.end())
#define FILL(a,d) memset(a,d,sizeof(a))
#define LL long long
#define PI 2*acos(0.0)
#define pi pair<int,int>
using namespace std;

int main()
{
   freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
  LL t,kk=0;
  cin>>t;
  while(t--)
  {
      LL x=-1,y=-1,c=0,fa=0;
      string s[10];
      for(LL i=0;i<4;i++)
        {
            cin>>s[i];
            for(LL j=0;j<4;j++)
            {
                if(s[i][j]!='.') c++;
            }
        }
       LL f=1;
       for(LL i=0;i<4;i++)
       {
           LL x,o,t;
           x=o=t=0;
           for(LL j=0;j<4;j++)
           {
               if(s[i][j]=='X')
                x++;
               if(s[i][j]=='O')
                o++;
               if(s[i][j]=='T')
                t++;
           }
           if(x==4) fa=1;
           else if(x==3&&t==1) fa=1;
           else if(o==4) fa=2;
           else if(o==3&&t==1) fa=2;
           x=o=t=0;
           for(LL j=0;j<4;j++)
           {
               if(s[j][i]=='X')
                x++;
               if(s[j][i]=='O')
                o++;
               if(s[j][i]=='T')
                t++;
           }
           if(x==4) fa=1;
           else if(x==3&&t==1) fa=1;
           else if(o==4) fa=2;
           else if(o==3&&t==1) fa=2;
       }
       cout<<"Case #"<<++kk<<": ";
       if(fa==1)
        cout<<"X won"<<endl;
       else if(fa==2)
        cout<<"O won"<<endl;
       else
       {
            LL x,o,t;
           x=o=t=0;
           for(LL i=0;i<4;i++)
           {
               if(s[i][i]=='X') x++;
               if(s[i][i]=='O') o++;
                if(s[i][i]=='T') t++;

           }
           if(x==4) fa=1;
           else if(x==3&&t==1) fa=1;
           else if(o==4) fa=2;
           else if(o==3&&t==1) fa=2;
           x=o=t=0;
           for(LL i=0;i<4;i++)
           {
               if(s[i][3-i]=='X') x++;
               if(s[i][3-i]=='O') o++;
                if(s[i][3-i]=='T') t++;
           }
           if(x==4) fa=1;
           else if(x==3&&t==1) fa=1;
           else if(o==4) fa=2;
           else if(o==3&&t==1) fa=2;

           if(fa==1)
        cout<<"X won"<<endl;
       else if(fa==2)
        cout<<"O won"<<endl;
        else if(c==16)
            cout<<"Draw"<<endl;
        else
            cout<<"Game has not completed"<<endl;
       }
  }
    return 0;
}
