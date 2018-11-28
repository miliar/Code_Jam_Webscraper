#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector < long long > vll;
typedef unsigned long long ull;
typedef pair < long long,  long long > pll;
typedef pair < int,  int > pii;
typedef vector < int > vii;

#define ff first
#define ss second
#define sz size()
#define clr clear()
#define len length()
#define pb push_back
#define mp make_pair

const int N = 1e5 + 500;
const ll mod = 1e9 + 7;
const ll INF = 1LL << 57LL;

//Fast expo

ll expo(ll a , ll b)
{
    if(b==0)
        return 1;
    else if(b%2==0)
        return expo(a*a,b/2);
    else
        return a*expo(a*a,b/2);
}

//comparing pair wrt to 2nd

bool compare(const pii &i, const pii &j)
{
    return i.ss < j.ss;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ifstream infile;
    ofstream outfile;
    infile.open("A-large.in");
    outfile.open("outfile.txt");
    int t;
    infile>>t;
    ll p=t;
    while(t--)
    {
        ll n;
        infile>>n;
        if(n==0)
        {
            outfile<<"Case #"<<p-t<<": INSOMNIA"<<endl;
        }
        else
        {
            set<int> s;
            ll m=1,k,ans=n;
            while(s.size()!=10)
            {
            k=n*m;
            ans=k;
            while(k!=0)
            {
                s.insert(k%10);
                k=k/10;
            }
            m++;
            }
            outfile<<"Case #"<<p-t<<": "<<ans<<endl;
            //cout<<n<<" Case #"<<p-t<<": "<<ans<<endl;
        }
    }
    infile.close();
    outfile.close();
    return 0;
}
