#include <bits/stdc++.h>
#define ll long long
#define dbg(x) cout<<#x<<": "<<x<<endl
#define dbgv(x,i) cout<<#x<<"["<<i<<"]: "<< x[i]<<endl
#define pii pair< int , int >
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define si(n) scanf("%d" , &n)
#define inf 1061109567
#define mod 1000000007
#define maxx 1000002
using namespace std;
char arr[10002];
int main()
{
    //ofstream fout("op.txt");
    //ifstream fin("in.txt");

    #ifndef ONLINE_JUDGE
    freopen("inp.txt","r",stdin);
    freopen("outp.txt", "w", stdout);
    #endif


    int i, j, k, src, dest, p, a,x, b, w, t, m, n,  v, ans, ans2, l, r, sum;
    scanf("%d", &t);
    for(k = 1; k <= t; k++)
    {
        scanf("%d %s", &n, arr);



        for(i = 0; i <= n; i++)
        {
            arr[i] -= '0';
        }
        sum = arr[0];
        ans = 0;
        for(i = 1; i <= n; i++)
        {

            if(sum < i)
            {

                ans += (i - sum);
                sum = arr[i] + i;
                //dbg(sum);
                //dbg(ans);
            }

            else sum = sum + arr[i];

        }

        printf("Case #%d: %d\n", k, ans);



    }






	return 0;
}
