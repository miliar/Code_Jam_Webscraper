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
map<int, bool> seen;
bool sdig[10];

int main()
{
    #ifndef ONLINE_JUDGE
    //freopen("C:\\Users\\yashvir\\Downloads\\A-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    //freopen("out.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    int t, i, j, k, n, f, x;
    scanf("%d", &t);
    rep(i, t)
    {
        printf("Case #%d: ", i+1);
        scanf("%d", &n);
        //seen[n]=true;
        x=n;
        for(j=x; j>0; j/=10) { sdig[j%10]=true; }
        f=1;
        while(1)
        {
            if(x==0) { f=0; break; }
            x+=n;
            //seen[x]=true;
            for(j=x; j>0; j/=10) { sdig[j%10]=true; }
            for(j=0; j<10; j++) if(!sdig[j]) break;
            if(j==10) break;
        }
        if(f) printf("%d\n", x);
        else printf("INSOMNIA\n");
        for(j=0; j<10; j++) sdig[j]=0;
    }
    return 0;
}
