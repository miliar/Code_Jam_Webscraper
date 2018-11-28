#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <functional>
#include <bitset>
#include <numeric>
#include <utility>
#include <sstream>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iomanip>

using namespace std;

bool can_win(const int N, const long long P,const long long higher)
{
    if(!(higher+1 <= (1LL << N))){*(char *)(3) = 2;}
    if(P <= 0){return false;}
    if(P >= (1LL<<N)){return true;}
    if(N == 0){return false;}
    const long long lower = (1LL<<N)-higher-1;
    //win your game?
    if(lower)
    {
        //you play a lower
        //minimize higher than you
        long long nhigh = higher - min((1LL<<(N-1))-1, higher/2);
        if(can_win(N-1, P, nhigh))return true;
    }
    //lose your game?
    if(higher)
    {
        //you play a higher
        //minimize higher than you
        long long nhigh = (higher - 1 - min(lower, higher-1))/2;
        if(can_win(N-1, P-(1LL<<(N-1)), nhigh)){return true;}
    }
    return false;
}

bool can_lose(const int N, const long long P,const long long higher)
{
    if(!(higher+1 <= (1LL << N))){*(char *)(3) = 2;}
    if(P <= 0){return true;}
    if(P >= (1LL<<N)){return false;}
    if(N == 0){return true;}
    const long long lower = (1LL<<N)-higher-1;
    //win your game?
    if(lower)
    {
        //you play a lower
        //maximize higher than you
        long long x = min((1LL << (N-1))-1, min(lower-1, higher));
        long long nhigh = x + (higher - x)/2;
        if(can_lose(N-1, P, nhigh))return true;
    }
    //lose your game?
    if(higher)
    {
        //you play a higher
        //maximize higher than you
        long long nhigh = min((1LL<<(N-1))-1, (higher - 1)/2);
        if(can_lose(N-1, P-(1LL<<(N-1)), nhigh)){return true;}
    }
    return false;
}

pair<long long, long long> solve_case(const int N, const long long P)
{
    pair<long long, long long> ret;
    {
        long long out = 0;
        for(int i=N-1;i>=0;--i)
        {
            if(can_lose(N, P, out+(1LL<<i)))
            {
                ;
            }
            else
            {
                out += (1LL<<i);
            }
        }
        ret.first = out;
    }
    {
        long long out = 0;
        for(int i=N-1;i>=0;--i)
        {
            if(can_win(N, P, out+(1LL<<i)))
            {
                out += (1LL << i);
            }
            else
            {
            }
        }
        ret.second = out;
    }
    return ret;
}

int main(int argc, char **argv)
{
    int CASES;
    cin >> CASES;
    for(int cn=1;cn<=CASES;++cn)
    {
        long long N,P;
        cin >> N >> P;
        pair<long long, long long> out = solve_case(N,P);
        printf("Case #%d: %lld %lld\n", cn, out.first, out.second);
    }
    return 0;
}
