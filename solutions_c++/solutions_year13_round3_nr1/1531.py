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
    int t,n;
    string s;
    cin>>t;
    FOR(k,1,t+1)
    {
        cin>>s>>n;
        int l =s.length();
        int hash[l+1];
        FOR(i,0,l)
        {
            if(s[i]!='a' && s[i]!= 'e' && s[i] !='i' && s[i]!='o' && s[i]!='u')
            hash[i]=1;
            else hash[i]=0;
        }
        LL ans=0;
        FOR(i,0,l)
        {
            int count=0;
            int max1=0;
            FOR(j,i,l)
            {
                if(hash[j]==1) count++;
                else count=0;
                if(count>max1) max1=count;
                if(max1>=n) 
                {
                    ans+=(l-j);
                    break;
                }    
            }
        }
        cout<<"Case #"<<k<<": "<<ans<<"\n";
   }
   return 0;    
}    
    
