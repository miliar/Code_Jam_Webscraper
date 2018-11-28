#include <iostream>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <string>
#define ll long long
#define MAX_SIZE 1000005
using namespace std;

const ll size = 1000001;

ll jumps[MAX_SIZE];


ll flip (ll a)
{
    string wrk = to_string(a);
    string res;
    ll j = 0;
    for (ll i = wrk.length()-1; i >= 0 ; i--)
    {
        res[j] = wrk[i];
        j++;
    }
    return stoll(res);
}

bool zeros (ll a)
{
    string wrk = to_string(a);
    ll base = 1;
    for (ll i = wrk.length()-1; i >= 0; i--)
    {
        if (wrk[i] == '0')
        {
            base *= 10;
        }
        else
        {
            break;
        }
    }
    return (base > 1);
}

void countJumps ()
{
    for (ll i = 1; i < size; i++)
    {
        jumps[i] = i;
    }
    ll w;
    for (ll i = 1; i < size; i++)
    {
        if (!zeros(i))
        {
            w = flip(i);
            jumps[i] = (min ((jumps[w]), (jumps[i-1]))) + 1;
        }
        else
        {
            jumps[i] = jumps[i-1] + 1;
        }

    }

}

int main()
{
    ll T, n;
    cin >> T;
    countJumps();
    for (ll i = 1; i <= T; i++)
    {
        cin >> n;
        cout << "Case #" << i << ": " << jumps[n] << endl;
    }
}