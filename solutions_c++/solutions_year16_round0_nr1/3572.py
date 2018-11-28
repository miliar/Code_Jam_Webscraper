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

static int dig[10];

int main()
{
    int T;
    scanf("%d", &T);
    for(int ctr=1; ctr<=T; ctr++)
    {
        ll N;
        cin>>N;
        if(N==0)
        {
            cout<<"Case #"<<ctr<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        memset(dig, 0, sizeof(dig));
        int cnt = 0;
        ll res = 0;
        do{
            res += N;
            int x;
            ll tmp = res;
            while(tmp>0)
            {
                x = tmp%10;
                tmp/=10;
                if(dig[x]==0)
                {
                    dig[x] = 1;
                    cnt++;
                }
            }
        }while(cnt<10);
        cout<<"Case #"<<ctr<<": "<<res<<endl;
    }
    return 0;
}
