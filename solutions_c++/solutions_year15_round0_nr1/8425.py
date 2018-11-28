#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<set>
#include<map>
#include<climits>
#include<cstring>
#include<list>
#include<fstream>
#include<queue>
#include<sstream>


using namespace std;

typedef long long LL;
typedef unsigned int UI;

LL mod=1e9 + 7;


int main()
{
      ios_base::sync_with_stdio(false);

      ifstream cin("A-large.in");
      ofstream cout("file.txt");


      int t;
      cin>>t;
      for(int I=0; I<t; I++)
      {
          int n;
          cin>>n;
          string s;
          cin>>s;
          vector <int> cum(n+1);
          cum[1]=s[0]-'0';
          for(int i=2; i<=n; i++)
          {
              cum[i]=cum[i-1]+(s[i-1]-'0');
          }

          int ret=0;

          for(int i=1; i<=n; i++)
          {
              if(cum[i]<i)
                {
                    ret+=abs(cum[i]-i);
                    for(int j=i+1; j<=n; j++)
                        cum[j]+=abs(cum[i]-i);
                }
          }

          cout<<"Case #"<<I+1<<": "<<ret<<'\n';


      }



}










