#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

#define FOR(k,x,n) for(long long k=x;k<n;k++)
#define SORT(x) sort(x.begin(),x.end())

using namespace std;
bool ispal(long long x);

int main()
{
    ios_base::sync_with_stdio(false);

    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);

    long long T,cases=1;
    cin>>T;
    long long sqpal[]={
    1,
    4,
    9,
    121,
    484,
    10201,
    12321,
    14641,
    40804,
    44944,
    1002001,
    1234321,
    4008004,
    100020001,
    102030201,
    104060401,
    121242121,
    123454321,
    125686521,
    400080004,
    404090404,
    10000200001,
    10221412201,
    12102420121,
    12345654321,
    40000800004,
    1000002000001,
    1002003002001,
    1004006004001,
    1020304030201,
    1022325232201,
    1024348434201,
    1210024200121,
    1212225222121,
    1214428244121,
    1232346432321,
    1234567654321,
    4000008000004,
    4004009004004
    };

    for(long long h=0;h<T;h++){

    long long a,b,c=0;
    cin>>a>>b;


    for(long long k=0;k<39;k++){

    if( sqpal[k] >=a && sqpal[k] <=b  ){
    //cout<<val<<endl;
    c++;
    }

    }
    cout<<"Case #"<<cases<<": "<<c<<endl;
    cases++;
    }

    return 0;
}

bool ispal(long long x){

long long aux=x;
long long res=0;

while(aux>0){
res+=aux%10;
aux/=10;
if(aux>0)
res*=10;
}

if(res==x)return true;
return false;
}
