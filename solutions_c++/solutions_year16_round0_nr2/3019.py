/* ***************************
Author: Abhay Mangal (abhay26)
*************************** */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <numeric>
#include <utility>
#include <bitset>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
 #define tr(container, it) \
    for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define maX(a,b) (a) > (b) ? (a) : (b)
#define pii pair< int, int >
#define pip pair< int, pii >
#define pll pair < ll, ll >
#define pill pair< int, pll >
#define FOR(i,n) for(int i=0; i<(int)n ;i++)
#define REP(i,a,n) for(int i=a;i<(int)n;i++)
#define pb push_back
#define mp make_pair
typedef long long ll;
char S[105];
int A[105];
int n;
void swapAll(int J, int K)
{
    for(int j=J,k=K;j<=k;j++,k--){
        if(j == k){
            A[j] = 1 - A[j];
        }
        else
        {
            A[j] = 1 - A[j];
            A[k] = 1 - A[k];
            swap(A[j], A[k]);
        }
    }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("3.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        scanf("%s", S);
        n = strlen(S);
        printf("Case #%d: ", z);
        for(int i=0;i<n;i++){
            if(S[i] == '+')
                A[i] = 0;
            else
                A[i] = 1;
        }
        int cnt = 0;
        for(int i=n-1;i>=0;i--){
            if(A[i] == 0)
                continue;
            if(A[0] == 0){
                cnt++;
                int j = 0;
                int k = j;
                for(int q=i-1;q>=j;q--)
                {
                    if(A[q] == 0)
                    {
                        k = q;
                        break;
                    }
                }
                swapAll(j,k);
            }
            cnt++;
            swapAll(0,i);

        }
        printf("%d\n",cnt);
    }
    return 0;
}
