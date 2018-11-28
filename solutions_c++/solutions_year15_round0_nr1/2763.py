#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;
const int N = 1050;

char S[N];
int S_max;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int x=1; x<=t; x++)
    {
        scanf("%d", &S_max);
        scanf("%s", S);
        int ret = 0;
        int sum = 0;
        for(int i=0; i<=S_max; i++)
        {
            if(sum >= i)
            {
                sum += S[i] - '0';
            }
            else if(S[i] > '0')
            {
                ret += i-sum;
                sum = i+S[i]-'0';
            }
            //cout<<i<<"  "<<ret<<endl;
        }
        printf("Case #%d: %d\n", x, ret);
    }
    return 0;
}
