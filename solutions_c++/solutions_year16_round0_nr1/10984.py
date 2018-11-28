#include<bits/stdc++.h>

#define all(a) (a).begin(), (a).end()
#define allr(a) (a).rbegin(), (a).rend()
#define x first
#define y second

#define oo 1e9
#define pi acos(-1)
#define MOD 1000000007

using namespace std ;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }
typedef pair<int, int> ii ;
typedef vector<ii> vii ;
typedef vector<int> vi ;


int main() {
   // ios_base::sync_with_stdio (false);
   freopen("a.in","r",stdin) ;
    freopen("a.out","w", stdout) ;
    int t,r,p=0,i=0;
    long long int c,q,ans;
    cin>>t;
    //cout<<t<<endl;
    int n;
    while(t--)
    {
        bool tab[10];bool b=true;
        i=0;
        memset(tab,false,sizeof(tab));
        cin>>n;
        //cout<<n<<endl;
        if(n==0)
        {
            p++;
            cout<<"Case #"<<p<<": "<<"INSOMNIA"<<endl;
        }
        else
        {
            b=true;
            while(true)
            {
                i++;
                //cout<<i<<endl;
                q=i*n;
                c=q;
                while(q!=0)
                {
                    r=q%10;
                    q=q/10;
                    tab[r]=true;
                    b=true;
                    for(int j=0;j<10;j++)
                    {
                        if(tab[j]==false)
                        {
                            b=false;
                        }
                    }
                    if(b==true)
                    {
                        //cout<<"--"<<endl;
                        ans=c;
                        p++;
                        cout<<"Case #"<<p<<": "<<ans<<endl;
                        break;
                    }
                }
                if(b==true)
                    break;
            }
        }
    }
    ///cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl ;
     return 0;
}
