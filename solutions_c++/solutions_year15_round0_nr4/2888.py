#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <set>
#include <map>
using namespace std;

void print(int i , string str)
{
    cout<<"Case #"<<i<<": "<<str<<'\n';
}

int main()
{
    ios::sync_with_stdio(false);
    int test;
    cin>>test;
    string gab = "GABRIEL";
    string rich = "RICHARD";
     for(int i = 1; i <=test; i++)
     {
             int x, r ,c;
             cin>>x>>r>>c;
             if(x==1)
             {
                 print(i,gab);
                 continue;
             }
             else if(x==2)
             {
                 if((r*c)<2 || (r*c)%2!=0)
                 {
                     print(i,rich);
                     continue;
                 }
                 else
                 {
                     print(i,gab);
                     continue;
                 }
             }
             else if(x==3)
             {
                 if((r*c)<3 || (r*c)%3!=0 || (r==1 || c==1))
                 {
                     print(i,rich);
                     continue;
                 }
                 else
                 {
                     print(i,gab);
                     continue;
                 }
             }
             else
             {
                 if((r*c)>11) print(i,gab);
                 else print(i,rich);
                 continue;
             }
     }
}
