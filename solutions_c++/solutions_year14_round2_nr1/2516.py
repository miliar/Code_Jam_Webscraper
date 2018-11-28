#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <cassert>
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
#include <cstring>
#include<stdio.h>

#define uniq(c) (c).resize(unique(c.begin(),c.end())-(c).begin());
#define all(a) a.begin(),a.end()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define PI 3.14159265
#define eps 1e-10
#define LL long long
#define ULL unsigned long long
#define MOD 1000000007



using namespace std;
int SI(string str) {int ans; stringstream s; s<<str; s>>ans; return ans;}
string IS(int n) {string str; stringstream s; s<<n; s>>str; return str;}


int main()
{
  freopen("read.txt","r",stdin);
  freopen("write.txt","w",stdout);
  
  //  cout<<"aabb" - "ab";

    int t,n;
    cin>>t;
    FOR(tt,1,t+1)
    {
        cin>>n;
        string a,b;
        cin>>a>>b;
        int l1 = a.length();
        int l2 = b.length();
        int i = 0,j = 0;
        int ans = 0;
        int flag = 0;
        while(i<l1 && j< l2)
        {
            if(a[i] != b[j]) 
            {
                flag = 1;
                break;
            }    
           int r1 = 0,r2 = 0;
           while(a[i+1] == a[i] && i+1<l1)
           {
               i++;
               r1++;
           }
           while(b[j+1] == b[j] && j+1<l2)
           {
               j++;
               r2++;
           }
           i++;j++;
           
           ans += abs(r1-r2);
        }
        if(flag == 0 && i==l1 && j==l2) cout<<"Case #"<<tt<<": "<<ans<<"\n";
        else //if(flag ==1 || (i!=l1 && j!=l2))
         cout<<"Case #"<<tt<<": "<<"Fegla Won"<<"\n";
        //if(ans<=max(l1,l2)) 
        
        
       
    }
    
 
    
    
    
  return 0;
    
}
