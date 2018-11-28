#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <iomanip>
#include <fstream>

typedef long long int ll;
ll gcd(ll a, ll b){ if(!b) return a; return gcd(b,a%b);}
using namespace std;

int main()
{ 
    ifstream  in("input.txt");
    ofstream out("output.txt");
    
    int l,t;
    in>>t;
    for(l=1;l<=t;l++)
    {
       double c,f,x;
       double curr, rate, time;
       
       curr=0.0;
       rate=2.0;
       time=0.0;
       
       in>>c>>f>>x;
       
       while(1)
       {
              double time_with_buy;
              double time_without_buy; 
              
              time_with_buy = c/rate + x/(rate+f);
              time_without_buy = x/rate;
              
              if(time_with_buy <= time_without_buy)
              {
                   time += c/rate;
                   rate += f;
              }
              else
              {
                  time += time_without_buy;
                  break;
              }
        }
        out<<"Case #"<<l<<": "<<setprecision(100)<<time;
        if(l<t) out<<endl;
    }
return 0;
}
