#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <utility>
#include <cassert>
#define mymin(a, b) (((a)<(b)) ? (a) : (b))

using namespace std;

int main(int argc, char* argv[])
{
    cin.precision(20);
    cout.precision(20);
    (void)argc; (void)argv;
    FILE* useless;
    useless=freopen("B-large.in", "r", stdin);
    useless=freopen("B-large.out", "w", stdout);
    assert(useless!=NULL);
    int t;
    cin >> t;
    for(int maiusato=1; maiusato<=t; maiusato++)
    {
        long double c, f, x, actGain=2.0;
        cin >> c;
        cin >> f;
        cin >> x;
        long double bestTime=x/actGain;
        long double totExtraTime=0.0;
        while(true)
        {
            totExtraTime+=c/actGain;
            actGain+=f;
            long double thisTime=(x/actGain)+totExtraTime;
            if(thisTime<=bestTime)
                bestTime=thisTime;
            else
                break;
        }
        cout << "Case #" << maiusato << ": " << bestTime;
        if(maiusato!=t)
            cout << endl;
    }
    return 0;
}
