/*********************
****SHASHANK GUPTA****
***@(my_blue_luck)****
**********************/

#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef long long int ll;

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    ll t,n,z,c,i,temp,m,x;
    cin >> t;
    for(x=1;x<=t;x++)
    {
        cin >> n ;
        m=n;
        bool cnt[10];
        ll flag=1;
        memset(cnt,false,sizeof(cnt));
        if(n==0)
        {
            cout << "Case #" << x << ": " << "INSOMNIA" << endl ;
            continue;
        }
        while(flag)
        {
            temp=n;
            while(temp)
            {
                z=temp%10;
                cnt[z]=true;
                temp=temp/10;
            }
            c=0;
            for(i=0;i<10;i++)
            {
                if(cnt[i]==true)
                    c++;
            }
            if(c==10)
            {
                cout << "Case #" << x << ": " <<  n << endl ;
                break;
            }
            else
            n+=m;
        }
    }
    return 0;
}
