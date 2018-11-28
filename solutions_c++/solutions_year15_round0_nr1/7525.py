#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <algorithm>
#include <sstream>
#define rep(x,y) for(int i=x;i<y;i++)
#define MAX 1007
using namespace std;

int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("A-large.out","wt",stdout);

    int T;
    cin>>T;;
    for(int test = 0; test < T; test++)
    {
        int N;
        cin>>N;
        long audience = 0, c = 0;
        char s[MAX];
        cin>>s;
        if(s[0] == '0')
        {
            c++;
            audience++;
        }
        rep(1,N+1)
        {
            int x = s[i-1] - 48;
            audience += x;
            if(i > audience && s[i] != '0')
            {
                int y = i - audience;
                c = c + y;
                audience = audience + y;
            }
        }
        cout << "Case #" << test + 1 << ": " << c << endl;
    }
    return 0;
}
