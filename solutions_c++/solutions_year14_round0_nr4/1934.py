#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<set>
#include<map>
#include<utility>
#include<vector>
#include<string>
#include<stack>
#include<queue>
using namespace std;
vector < int > A,B;
void scan(int N, vector < int > &V)
{
    double x;
    while (N--)
    {
        scanf("%lf", &x);
        x = x * 100000;
        V.push_back((int) x);
    }
}
int dwar(int N)
{
    vector < int > AA = A;
    int i,j, ans = 0;
    for (i=N-1; i>=0; --i)
    {
        for (j=0; j<N; ++j)
        {
            if (AA[j] > B[i]) break;
        }
        if (j < N)
        {
            //printf("%d %d\n", A[i], BB[j]);
            AA[j] = -1;
            ++ans;
        }
        else
        {
            for (j=0; j<N; ++j)
            {
                if (AA[j] != -1) break;
            }
            AA[j] = -1;
        }
    }
    return ans;
}
int war(int N)
{
    vector < int > BB = B;
    int i,j, ans = 0;
    for (i=0; i<N; ++i)
    {
        for (j=0; j<N; ++j)
        {
            if (BB[j] > A[i]) break;
        }
        if (j < N) BB[j] = -1;
        else ++ans;
    }
    return ans;
}
int main()
{
    //freopen("data.txt", "r", stdin);
    freopen("Din.txt", "r", stdin);
    freopen("Dout.txt", "w", stdout);
    int t,T;
    int N,i;
    double x;
    scanf("%d", &T);
    for (t=1; t<=T; ++t)
    {
        scanf("%d", &N);
        A.clear(), B.clear();
        scan(N,A); scan(N,B);
        sort (A.begin(), A.end()), sort (B.begin(), B.end());
        printf("Case #%d: %d %d\n", t, dwar(N), war(N));
    }
    return 0;
}
