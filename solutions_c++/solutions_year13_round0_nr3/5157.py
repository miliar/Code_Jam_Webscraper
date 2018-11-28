#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <climits>
#include <bitset>
#include <string>
#include <iostream>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <list>
#include <cstring>
#define mod 1000000007
using namespace std;
set <long long int> s;
bool p (long long int x)
{
    long long int a=x,b=0;
    while (x != 0) {
        b = b*10 + (x%10);
        x =x/10;
    }
    if (a == b) {
        return true;
    }
    return false;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    long long int t,i,x,y,ii=1;
    cin >> t;
    for (i = 1; i <= 10000000; i++) {
        if (p (i) && p (i*i)) {
            s.insert (i*i);
        }
    }
    while (t--) {
        long long int sum = 0;
        cin >> x >> y;
        cout << "Case #" << ii << ": ";
        ii++;

        set <long long int> :: iterator it;
        for (it = s.begin(); it != s.end(); it++) {
            if ((*it) >= x && (*it) <= y) {
                sum++;
            }
        }
        cout << sum << endl;
    }

    return 0;
}
