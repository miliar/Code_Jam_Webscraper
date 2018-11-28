#include<bits/stdc++.h>

#define mod 1000000007
#define inf 1000000009
#define MX 1000001

#define pb push_back
#define mp make_pair
#define ll long long
#define gc getchar
#define vi vector<int>
#define rep(i, n) for(int i=0; i<n; i++)

using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("C:\\Users\\yashvir\\Downloads\\D-small-attempt0.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    int t, i, j, k, c, s;
    scanf("%d", &t);
    rep(i, t)
    {
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d: ", i+1);
        for(j=1; j<=k; j++) printf(" %d", j);
        printf("\n");
    }
    return 0;
}
