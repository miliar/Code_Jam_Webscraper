#include<iostream>
#include<math.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<queue>
#include<sstream>
#include<ctime>
using namespace std;

typedef long long ll;
typedef long long int lli;
#define mp make_pair
#define pb push_back

const int maxint=60000;

int main()
{
    freopen("inp-large.in", "r", stdin);
    freopen("inp.out", "w", stdout);
    double C,F,X;
    int n;
    cin>>n;
    int start = 1;
    while(start<=n){
        double max_t, p=2.0, buy_t, t;
        cin>>C>>F>>X;
        max_t = X/2.0;
        buy_t = 0.0; t = 0.0;
        while(1){
            buy_t += C/p;
            p += F;
            t = buy_t + X/p;
            if(t>=max_t) break;
            else max_t = t;
        }
        printf("Case #%d: %.7f\n",start,max_t);
        start++;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
