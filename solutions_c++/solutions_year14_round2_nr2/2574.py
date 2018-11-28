#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <bitset>
#include <cstring>
#include <vector>
#define INF 2147483647
#define NINF -2147483647
#define pb push_back
#define mp make_pair
#define LL long long
using namespace std;
int dp[1001][1001];
main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    for(int i=0;i<=1000;i++)
        for(int j=0;j<=1000;j++)
            dp[i][j]=i&j;
    for(int t=1;t<=T;t++){
        int A,B,K,res=0;
        cin >> A >> B >> K;
        for(int i=0;i<A;i++)
            for(int j=0;j<B;j++)
                if(dp[i][j]<K)
                    res++;
        printf("Case #%d: %d\n",t,res);
    }
}
