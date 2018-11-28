
/***** Author : Akshay *****/
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#include <cmath>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <numeric>
#include <map>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <set>
#include <fstream>

using namespace std;

#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)


#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define ALL(x) x.begin(), x.end()
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define INF 1000000000
#define MOD 10000007
#define toString(x) #x
#define add(a,b) toString(a##b)
//#define __ONLINE__JUDGE__ 1


typedef long long ll;
typedef pair<int,int> ii;
typedef pair<int, ii> Lii;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<string> VS;

int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};

/* Function for string split . If string starts with de-lim then call split(s.substr(1,s.length()),DELIM);
 *    else call split(s,DELIM);*/
std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while(std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}


std::vector<std::string> split(const std::string &s, char delim) 
{
    std::vector<std::string> elems;
    return split(s, delim, elems);
}

int iter,tc;
ll a,b;
const ll limit= 100000000000000;
vector<ll> nos;
bool isPallindrome(ll x)
{
    vector<int> t;
    while( x )
    {
        t.push_back(x%10);
        x/=10;
    }
    int sz = t.size();
    for(int i = 0 ; i < sz/2; i++ )
    {
        if( t[i] != t[sz-i-1] ) return false;
    }
    return true;
}
void preCompute(void)
{
    for(ll i=1;i*i<= limit;i++)
    {
        if(isPallindrome(i) && isPallindrome(i*i))
            nos.push_back(i*i);
    }
}
int main()
{
    preCompute();
    iter=1;
    scanf("%d",&tc);
    while(tc--)
    {
        scanf("%lld%lld",&a,&b);
        int ret=0;
        for(int i=0;i<(int)nos.size();i++)
        {
            if( nos[i] >=a && nos[i] <=b ) ret++;
        }
        printf("Case #%d: %d\n",iter,ret);
        iter++;
    }
    return 0;
}
