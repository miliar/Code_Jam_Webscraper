#include<bits/stdc++.h>
using namespace std;
//-------------------------------------

#define ll long long
#define sc(x) scanf("%lld",&x)
#define sc2(x,y) scanf("%lld%lld",&x,&y)
#define sci(x) scanf("%d",&x)
#define sci2(x,y) scanf("%d%d",&x,&y)

#define mem(x) memset(x,0,sizeof x)
#define all(x) x.begin(),x.end()
#define pb(x)  push_back(x);
#define xx first
#define yy second
#define inf 999999999999999
#define mkp(x,y) make_pair(x,y)
#define pii pair<ll,ll>

//---------------------------------------

#define MX 300007
#define pi 2*acos(0.00)

#define open       freopen("input.in","r",stdin)
#define close      freopen ("output.txt","w",stdout)


int main()
{
    ll i, j, l, u, v, w, x, y, z, a, b, c, d, e, f, t = 1, tc;
    ll flg, sz, cnt, gt, ans, mx, mn;
    ll m, k, n,df;
    ll low, hi, md, sm, ff,st1[20],st2[20],st3[20];
    open;
    close;
    sc(tc);
    getchar();
    while(tc--)
    {
        mem(st1);
        mem(st2);
        string st;

        cin >> st;
        sz = st.size();
        for(i=0; i<sz; i++)
        {
            if(st[i]=='+') st1[i]=1;
            else st1[i]=0;
        }
        int id;
        cnt = 0;
        for(i=0; i<=1000000; i++)
        {
            gt = 1;
            for(j=0; j<sz; j++)
            {
                gt*=st1[j];
                if(st1[j]) st2[j]=0;
                else st2[j]=1;
                if(!st1[j]) id = j;
            }
            if(gt) break;
            if(st1[0]==1)
            {
                for(j=0; j<sz; j++)
                {
                    if(st1[j]) st1[j]=0;
                    else
                    {
                        cnt++;
                        break;
                    }
                }
//            cout<<"A";
//            for(j=0;j<sz;j++) cout<<st1[j];cout<<endl;
                continue;
            }
//        cout<<id<<endl;
            k = 0;
            for(j=id; j>=0; j--)
            {
                st1[j]=st2[k],k++;
            }
            cnt++;
//        for(j=0;j<sz;j++) cout<<st1[j];cout<<endl;
        }
//    cout<<cnt<<endl;
        printf("Case #%lld: %lld\n",t++,cnt);
    }


    return 0;
}

