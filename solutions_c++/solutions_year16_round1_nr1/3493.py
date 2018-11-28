#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <numeric>
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
#include <cstring>
#include <climits>
#include <cassert>
#include <iostream>
#include <fstream>
#define MOD 1000000007
#define pi 3.141592653589
#define ii pair<int,int>
#define vii vector<ii>
#define ll  long long int
#define REP(i,a,b) for(ll i=a;i<=b;i++)
#define loop(i,n) for(ll i=0;i<n;i++)
#define ll  long long int
#define loop2(i,n) for(ll i=1;i<=n;i++)
#define MIN(a,b) (a) < (b) ? (a) : (b)
#define MAX(a,b) (a) > (b) ? (a) : (b)
#define ABS(a) (a) > 0 ? (a) : -(a)
using namespace std;




int main()
{
    
    ofstream fout("/Users/ashish/Desktop/Alarge-practice.out.txt");
    ifstream fin ("/Users/ashish/Desktop/A-large.in.txt");
    ll t;
    fin>>t;
    loop2(u, t){
        string s;
        fin>>s;
        ll y =s.length();
        string s1 = "";
        
        s1+=s[0];
        for(ll j=1;j<y;j++){
           
            if(s[j]>=s1[0]){
                s1 = s[j]+s1;
            }
            else{
                s1 = s1+s[j];
            }
    }
        
        fout<<"Case #"<<u<<": "<<s1<<endl;
        
    }
  
    
    
            return 0;
}