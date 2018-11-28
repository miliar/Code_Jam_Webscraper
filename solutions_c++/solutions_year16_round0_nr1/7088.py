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



ll arraydigits[10];

void increasedigits(ll n)
{
    while(n){
        ll y = n%10;
        arraydigits[y] = 1;
        n/=10;
    }
    
}



bool trueorfalse(){
    for(ll i=0;i<10;i++){
        if(arraydigits[i]==0){
            return false;
        }
    }
    return true;
}


int main()
{
    
    ofstream fout("/Users/ashish/Desktop/A-large-practice.out.txt");
    ifstream fin ("/Users/ashish/Desktop/A-large.in.txt");
    ll t;
    fin>>t;
    loop2(j, t){
        ll n;
        fin>>n;
        for(ll r = 0;r<10;r++){
            arraydigits[r] = 0 ;
        }
        if(n==0){
            fout<<"Case #"<<j<<":"<<" "<<"INSOMNIA"<<endl;
        }
        else{
            ll toadd = n ;
            bool flag  = true;
            increasedigits(n);
            while(flag){
                if(trueorfalse()==true){
                    flag = false;
                }
                else{
                    n+=toadd;
                    increasedigits(n);
                }
            }
            
            
            fout<<"Case #"<<j<<":"<<" "<<n<<endl;
        }
    }
    
    
            return 0;
}