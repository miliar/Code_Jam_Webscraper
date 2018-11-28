#include<cstdio>
#include<string>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cctype>
#include<set>
#include<queue>
#include<stack>
#include<list>

#include<iomanip>
#include<fstream>
#include<numeric>
#include<map>
#include<sstream>
#include<iterator>
#define M 100
using namespace std;
typedef long long  ll;
typedef double   llf;
void print(vector<llf> v)
{
    for( int i =0;i< v.size();i++)
        cout << v.at(i) <<" ";
    cout <<endl;
}
void get(vector<llf> &ni , ll k)
{
    int j;
    llf p;
    for(j =0;j< k ;j++)
    {
        cin >> p;
        ni.push_back(p);
    }
    sort(ni.begin(),ni.end());
//    print(ni);
}

int main()
{
    int n,ce=1;
	freopen("D:\\aa.in","r",stdin);
    freopen("D:\\out.txt","w",stdout);
	cin >> n;
	while (n--)
    {
        ll i,j,k;
        cin >> k;
         vector<llf> ni , mi, tn, tm;
         get(ni,k);
         get(mi,k);
         tn = ni ; tm = mi;
       // print(tn);
      //  print(tm);
         ll c =0;
         printf("Case #%d: ",ce++);
         for( i =0;  tm.size() ;i++)
         {
          //   print(tn);
         //   print(tm);
            if(tn.at(tn.size()-1)>tm.at(tm.size()-1))
            {
                tn.erase(tn.begin()+tn.size()-1);
                tm.erase(tm.begin()+tm.size()-1);
                c++;
                continue;
            }
            if(tn.at(0)<tm.at(tn.size()-1))
             {

                 tn.erase(tn.begin());

                 tm.erase(tm.begin()+tm.size()-1);

              //   cout << i <<endl;
             }

            // else break;
         }
         for(i =0; i<ni.size() ;)
         {
             for(j=0;j<mi.size();j++)
             {
                 if(ni.at(i)<mi.at(j))
                 {
                     ni.erase(ni.begin()+i);
                     mi.erase(mi.begin()+j);
                     break;
                 }
             }
             if(j==mi.size())i++;
         }

        cout <<c << " "<< mi.size()<<endl;
    }
}
