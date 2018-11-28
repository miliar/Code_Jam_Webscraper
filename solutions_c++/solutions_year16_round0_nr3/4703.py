#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define s(a) sort(a.begin(),a.end())
#define vecll vector<long long int>
#define vecs vector<string>
#define vecpll vector<pair<long long int,long long int> >
#define rep(i,a,b) for(long long int (i)=(a);(i)<(b);(i)++)
#define repr(i,b,a) for(long long int (i)=(b);(i)>=(a);(i)--)
#define fast_IO ios_base::sync_with_stdio(false);cin.tie(0);
#define while_tc long long int t;cin>>t;while(t--)
#define ispow2(n) (n&&(!(n&(n-1))))      ///check if its perfect power of 2
#define MOD 1000000007
typedef long long int ll;
using namespace std;
template <typename T>
T modpow(T base, T exp) {
  /// base %= modulus;
  T result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base); ///  % modulus;
    base = (base * base); ///  % modulus;
    exp >>= 1;
  }
  return result;
}


int main()
{
    ll i,j,t,n,count;
    vecll v;
    vecll v1;
    vecll got;
    vecll got1;
    v.clear();
    rep(i,0,10000001)
        v.pb(1);
        //cout<<"S"<<endl;
    for (ll temp=2;temp*temp<=10000000;temp++)
    {
        for (ll temp1=temp;temp*temp1<=10000000;temp1++)
            v[temp*temp1]=0;
    }
    //cout<<"S"<<endl;
    rep(i,2,10000000)
        if (v[i]==1)
            v1.pb(i);
    queue <string> s;
    //queue <string> :: iterator it;
    s.push("1");
    rep(i,2,16)
    {
        while((s.front()).length()!=i)
        {
            s.push(s.front()+"1");
            s.push(s.front()+"0");
            s.pop();
        }
    }
    while (s.front().length()!=16)
    {
        s.push(s.front()+"1");
        s.pop();
    }
    //rep(i,0,v1.size())
    //cout<<v1[i]<<" ";
    freopen("C-small-attempt1.in","r",stdin);
	freopen("output1.txt","w",stdout);
	fast_IO
	cin>>t;
	cin>>n>>j;
	count=0;
	cout<<"Case #1:"<<endl;
	//vecll got;

        while(!s.empty())
        {
            bool ha=true;
            //cout<<s.front()<<" ";
            rep(p,2,11)
            {
                ll fo;
                ha=true;
                ll x=0;
                rep(i,0,16)
                {
                    if ((s.front())[15-i]=='1')
                        {
                            ll hoho=1;
                            ll f=i;
                            while(f--)
                                hoho*=p;
                            x+=hoho;
                        }
                }
                rep(i,1,v1.size())
                    {
                        if (x%v1[i]==0)
                            {
                                fo=v1[i];
                                ha=false;
                            }
                        if (!ha)
                                break;
                    }
                //if (v[x]==1)
                    //ha=false;
                //else
                    //got.pb(v1[x]);
                    if (!ha)
                    {
                        if (fo !=1 && fo<x)
                        {
                            got.pb(fo);
                            got1.pb(x);
                        }
                    }
                    else
                        break;
                    	//cout<<"R"<<endl;

            }
            rep(i,0,9)
                if (got[i]>1000)
                    ha=true;
            if (!ha && got.size()==9)
            {
                count+=1;
                cout<<s.front()<<" ";
                rep(i,0,9)
                    cout<<got[i]<<" ";
                cout<<endl;
            }
            /**if (ha)
                {
                    count+=1;
                    cout<<(s.front())<<" ";
                    rep(i,0,9)
                        cout<<got[i]<<" ";
                    cout<<endl;
                }
                */
                got.clear();
                got1.clear();
                s.pop();
            if (count==50)
                break;
        }
	return 0;
}
