#include <bits/stdc++.h>
#define INF 1000000000
#define mod 1000000007
#define vi vector<int>
#define vit vector<int>::iterator
#define ll long long
#define ii pair<int, int>
#define vii vector<ii>
#define pb push_back
#define mp make_pair
using namespace std;

static int a[3000];

int main()
{
    int T;
    scanf("%d", &T);
    for(int ctr=1; ctr<=T; ctr++)
    {
        int N, i, j, num;
        scanf("%d", &N);
        int lim = 2*N-1;
        memset(a, 0, sizeof(a));
        for(i=0; i<lim; i++)
            for(j=0; j<N; j++)
                {
                    scanf("%d", &num);
                    a[num]++;
                }
        vi v;
        for(i=0; i<=2500; i++)
        {
            if(a[i]%2==0)
                continue;
            v.pb(i);
        }
        cout<<"Case #"<<ctr<<":";
        for(vit it = v.begin(); it!=v.end(); it++)
            cout<<" "<<(*it);
        cout<<endl;
    }
    return 0;
}
