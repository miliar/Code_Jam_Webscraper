#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<ctime>

#define LL long long
#define FOR(n) for(int i = 0;i < n;i++)

using namespace std;

int recount(string audience, int n)
{
    int sum = 0;
    for(int i =0;i < n;i++)
        sum += (audience.at(i)-48);
    return sum;
}

int main()
{
    int t = 0, s = 0, need;
    string audience;
    cin >> t;
    FOR(t)
    {
        cin >> s >> audience;
        need = 0;
        for(int j = 1;j < s+1;j++)
            while(recount(audience, j) + need < j) need++;
        cout << "Case #" << i+1 << ": " << need << endl;
    }
    return 0;
}
