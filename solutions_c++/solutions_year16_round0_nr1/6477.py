#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>
#include<cstring>


using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size


#define pf printf
#define sf scanf

int getAns(int n) {
    if (n==0)
        return -1;
    int sum = n;
    int counter = 0;
    bool flag[10];
    fill(flag, flag+10, false);
    while ( true) {
        int sumDig = sum;
        while ( sumDig) {
            if ( flag[sumDig%10] == false) {
                counter++;
                flag[sumDig%10] = true;
                if ( counter == 10)
                    return sum;
            }
            sumDig /= 10;
        }
        sum = sum+n;
    }
}

int main()
{
    //freopen("in.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("ans.txt","w",stdout);

    int kase = 1;

    int test;
    cin>>test;
    while ( test--) {
        int n;
        cin>>n;
        int ans = getAns(n);
        if (ans == -1)
            pf("Case #%d: INSOMNIA\n", kase++);
        else
            pf("Case #%d: %d\n",kase++,ans);
    }
    return 0;
}
