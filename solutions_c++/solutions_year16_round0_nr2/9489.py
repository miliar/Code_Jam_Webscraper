//PD
#include<bits/stdc++.h>
#define pb push_back
#define SZ(a) (int)(a.size())
#define sortarr(a) sort(a.begin(),a.end()) 
#define sortrev(a) sort(a.rbegin(),a.rend())
#define mp make_pair
#define fi(i,a,b) for(i=a;i<b;i++)
#define X first
#define Y second

using namespace std;

typedef long long LL;
typedef vector<int> VI;
LL modpow(LL a, LL p, LL mod)
{LL ret = 1;while(p){if(p&1)ret = (ret*a)%mod;a=(a*a)%mod;p/=2;}return ret;}

LL power(LL a, LL p)
{LL ret = 1;while(p){if(p&1)ret = (ret*a);a=(a*a);p/=2;}return ret;}
/*int p[1000011];
VI prms;
void sieve(int n)
{int i,j;prms.pb(2);;fi(i,3,n){if(!i%2||!p[i])continue;prms.pb(i);for(j=2*i;j<n;j+=i)p[j]=1;}}*/


int main()
{
    int i,j,k,tmp;
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    int t,T;
    cin>>t;
    T=t;
    while(t--)
    {
        cout<<"Case #"<<T-t<<": ";
        string s;
        cin>>s;
        LL count=0;
        string::iterator it,it1;
        for(it=s.end()-1;it!=s.begin();it--)
        {
            if (*it=='-' &&  *s.begin()!='-')
            {
                count++;
                for(it1=s.begin();it1!=it;it1++)
                {
                    if(*it1=='+')
                        *it1='-';
                    else
                        break;
                }
                
            }
            if(*it=='-')
            {
                reverse(s.begin(), it+1);
                for(it1=s.begin();it1!=it+1;it1++)
                {

                    if(*it1=='+')
                        *it1='-';
                    else
                        *it1='+';
                }
                count++;
            }
        //    cout<<s<<endl;
        }
        if(*s.begin()!='+')
            count++;
        cout<<count<<endl;
    }


    return 0;
}

