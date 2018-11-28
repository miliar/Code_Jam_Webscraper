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
    

    freopen("c.in", "r", stdin);
    freopen("cc.out", "w", stdout);

    long long T,cases=1;
    cin>>T;
    for(long long h=0;h<T;h++){

    long long a,b;
    cin>>a>>b;

    vector<long long> pals;
    for(long long k=1;k<=sqrt(b);k++){

    if(ispal(k)) pals.push_back(k);

    }
    long long c=0;
    for(long long k=0;k<pals.size();k++){
    long long val=pals[k]*pals[k];

    if(ispal(val) && val<=b && val>=a ){
   // cout<<val<<endl;
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

