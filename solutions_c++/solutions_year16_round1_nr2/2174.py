#include<bits/stdc++.h>
#define ll long long int
#define PB push_back
#define F first
#define S second
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++) 
#define sint(n); scanf("%d",&n);
#define sll(n); scanf("%lld",&n);
#define pint(n); printf ("%d\n",n);
#define pll(n); printf ("%lld\n",n);
#define sst(n); scanf("%s",n);
#define pst(n); printf ("%s\n",n);
#define f(i,a,b) for(ll i=a;i<b;i++)
#define set(a,b) memset(a, b, sizeof(a))


using namespace std;

ll num;
vector < vector < ll > > arr, arr2;
ll arr3[150][150];
vector < ll > diag, psp;
ll found, flag=0;
void compute(ll x)
{
    vector < pair < ll, ll > > val;
    ll ct=0;
    tr(arr2, i)
    {
        auto xx=*i;
        auto yy = xx.begin()+x;
        ll zz = *yy;
        val.PB(make_pair(zz, ct++));
    }
    sort(val.begin(), val.end());
    tr(val, i)
    {
        auto xx=*i;
//        cout<<xx.F<<"("<<xx.S<<")"<<" ";
    }
//    cout<<endl;
    if (val.size()>1 && val[0].F==val[1].F)
    {
//        cout<<"removed "<<val[0].S<<" "<<val[1].S<<endl;
        ll fir=max(val[0].S, val[1].S), sec=min(val[0].S, val[1].S);
        arr2.erase(arr2.begin()+fir);
        arr2.erase(arr2.begin()+sec);
    }
    else
    {
        flag=1;
        auto xx = arr2.begin()+val[0].S;
        psp = *xx;
        num = val[0].F;
    }
/*    tr(arr2, i)
    {
        auto xx = *i;
        tr(xx, j)
        {
            cout<<*j<<" ";
        }
        cout<<endl;
    }
*/    return;
}

int main()
{
    ll tst;cin>>tst;
    vector < ll > tmp;
    f(t,1,tst+1)
    {
        psp.clear();arr.clear();arr2.clear();set(arr3, 0);
        found = -1;
        flag=0;
        ll n;
        cin>>n;
        f(i,0,2*n-1)
        {
            tmp.clear();
            ll tmp2;
            f(j,0,n)
            {
                sll(tmp2);
                arr3[i][j] = tmp2;
                tmp.PB(tmp2);
            }
            arr.PB(tmp);
            arr2.PB(tmp);
        }
        f(i,0,n)
        {
            compute(i);
            if (flag==1)
            {
                found = i;
                break;
            }
        }
        ll  ans[3000], maxm=-1;
        set(ans, 0);
        tr(arr, i)
        {
            auto zz = *i;
            auto yy = zz.begin()+found;
            ans[*yy]++;
        }
        tr(psp, i)
        {
            ans[*i]--;
        }
        ans[num]++;
        cout<<"Case #"<<t<<": ";
        for (ll i=2999;i>=0;i--)
            if (ans[i]>0)
            {
                maxm = i;
                break;
            }
        f(i,0,3000)
        {
            if (maxm>i && ans[i]>0)
                cout<<i<<" ";
            else if (maxm==i)
            {
                cout<<i<<endl;
                break;
            }
        }
    }
    return 0;
}
