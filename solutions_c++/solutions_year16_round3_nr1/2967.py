#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
     freopen("A-small-attempt0.in", "r", stdin);
     freopen("gcj1c2016aOutS.txt", "w", stdout);
     int tst;
     cin >> tst;
     string str="";
     vector< pair<int,char> > v;
     vector<string> vans;
     int ctr=0,tsen=0,n,nsen,ind;
     double maj=0.0;
     for(int i=1;i<=tst;i++)
     {
          cin >> n;ctr=0;tsen=0;
          v.clear();vans.clear();
          for(int j=1;j<=n;j++)
          {
               cin >>nsen;
               tsen+=nsen;
               v.push_back(make_pair(nsen,(char)(64+j)));

          }
          maj=tsen/2.0;
          sort(v.begin(),v.end());
          ind=v.size()-1;
          while(tsen>0)
          {

             if(maj-1>=(v[ind-1]).first)
               {
                  str=(str+v[ind].second)+v[ind].second;
                  vans.push_back(str);
                  (v[ind].first)-=2;
                  tsen-=2;maj-=1;sort(v.begin(),v.end());
               }
              else if((n>2)&&(maj-1<(v[ind-2]).first))
             {
                 str=v[ind].second;
                 vans.push_back(str);
                 (v[ind].first)-=1;sort(v.begin(),v.end());
                 tsen-=1;maj=tsen/2.0;
             }
               else //if(maj-1<(v[ind-1]).first)
               {
                  str=(str+v[ind].second)+v[ind-1].second;
                  vans.push_back(str);
                  (v[ind].first)-=1;(v[ind-1].first)-=1;
                  tsen-=2;maj-=1;sort(v.begin(),v.end());
               }
               str="";

          }
          cout <<"Case #"<<i<<": ";
          for(int k=0;k<vans.size();k++)
          {
             if(k==vans.size()-1)
               cout << vans[k] <<endl;
             else
                cout << vans[k] <<" ";
          }
     }
     return 0;
}
