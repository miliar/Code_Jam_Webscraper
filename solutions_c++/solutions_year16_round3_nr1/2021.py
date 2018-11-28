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

multiset<int> p;
int y[26];
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("J:\\Downloads\\A-large.in","r",stdin);
    //freopen("J:\\Downloads\\A-small-attempt1.in","r",stdin);
    freopen("out.txt", "w", stdout);
    //freopen("in.txt","r",stdin);
    #endif // ONLINE_JUDGE

    int t, i, j, k, n, sh, h, pos, poss, s;
    scanf("%d", &t);
    rep(q, t)
    {
        printf("Case #%d: ", q+1);
        scanf("%d", &n);
        for(i=0; i<n; i++) { scanf("%d", &y[i]); }
        sh=h=s=0;
        pos=poss=-1;
        for(i=0; i<n; i++)
        {
            if(y[i]>h) { sh=h; h=y[i]; poss=pos; pos=i; }
            else if(y[i]>sh) {sh=y[i]; poss=i;}
            s+=y[i];
        }
        if(s%2) { printf("%c ", pos+'A'); y[pos]--; }
        while(1)
        {
            sh=h=s=0;
            pos=poss=-1;
            for(i=0; i<n; i++)
            {
                if(y[i]>h) { sh=h; h=y[i]; poss=pos; pos=i; }
                else if(y[i]>sh) {sh=y[i]; poss=i;}
                s+=y[i];
            }
            if(h==0) break;
            y[pos]--;
            printf("%c",pos+'A');
            if(poss!=-1)
            {
                printf("%c ",poss+'A');
                y[poss]-=1;
            }
        }

        printf("\n");
    }
    return 0;
}
