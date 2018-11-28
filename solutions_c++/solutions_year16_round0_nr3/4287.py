#include <bits/stdc++.h>
///
///kill me PlZ !!!! i am a Shity code :( :(
//feeeling lonely in my life
///falled in love but from one side
//thing started to get really shit
///forever alone :(
using namespace std;
#define ll long long
const ll INF = (ll) LLONG_MAX;
//#define ln length()
#define pb push_back
#define sz size
#define mp make_pair
#define qq  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define all(n)   (n).begin(),(n).end()
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vll vector<pair<ll,ll> >
#define vi vector <int>
#define F first
#define S second
#define fcin(n,x) for(int i=0;i<n;cin>>x[i++])
#define fcout(n,x) for(int i=0;i<n;cout<<x[i++]<<" ")
#define cn(v) scanf("%d",&v)
#define cn2(v,w) scanf("%d %d",&v,&w)
#define cn3(v,w,z) scanf("%d %d %d",&v,&w,&z)
#define endl "\n"
#define EPS 1e-18
#define for2c(n,m,mat) for(int i=0;i<n;i++)for(int j=0;j<m;j++)cin>>mat[i][j];
#define fori(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); it++)
//directions
int dx[4] = { 0, -1, 0, 1 };
int dy[4] = { 1, 0, -1, 0 };
int dx8[9] = { 1,0,-1,0,1,-1,-1,1,0 };
int dy8[9] = {  0,1,0,-1,1,-1,1,-1,0};
///commenly used function s :) :) :) : )//
//priority_queue<int, vector<int>, std::greater<int> > first;
ll ipow(ll base,ll exp)
{
    ll result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}
string tos(ll n)
{
    stringstream ss;
    string ans;
    ss << n;
    ss >> ans;
    return ans;
}
ll toll(string n)
{
    return atoll(n.c_str());
}
double dist(double x1, double y1, double x2, double y2)
{
    return sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)));
}
int doubleCompare(double x, double y)
{
    if (fabs(x - y) <= EPS)
        return 0;

    if (x < y)
        return -1;

    return 1;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//new code ///////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
ll a[15][40];
bitset<1000000> primes;
vector<ll> allprim;
void seive(){
primes.set();
primes[0]=primes[1]=0;
for(int i=2;i * i<1000000;i++){
    for(int j=i*i;j<1000000;j+=i){
        primes[j]=0;
    }
}
for(ll i=2;i<1000000;i++){
if(primes[i])allprim.pb(i);
}
return ;

}
ll num2base(ll tmp, int base)
{
    bitset<16> test(tmp);
    int c=0;
    ll ret=0;
    for(int i=0; i<16; i++)
    {
        if(test[i])
        {
            ret+=a[base][c];
           // cout<<a[base][c]<<" "<<c<<" "<<base<<" "<<test<<endl;
        }
        c++;
    }
    return ret;
}
int main()
{
//////////
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    memset(a,0,sizeof a);
    seive();
    for(int i=0; i<=18; i++)
    {
        a[2][i]=ipow(2,i);
        a[3][i]=ipow(3,i);
        a[4][i]=ipow(4,i);
        a[5][i]=ipow(5,i);
        a[6][i]=ipow(6,i);
        a[7][i]=ipow(7,i);
        a[8][i]=ipow(8,i);
        a[9][i]=ipow(9,i);
        a[10][i]=ipow(10,i);
    }

    int tc;
    cin>>tc;
    for(int i=0; i<tc; i++)
    {
        int n,j;
        cin>>n>>j;
        for(ll k=((1<<(n-1))+1); k<(1<<(n))&&j; k+=2)
        {
            bool f=1;
            vector<ll> ans;
            for(int y=1; y<10; y++)
            {
                ll num=num2base(k,y+1);

                if(num<1000000&&primes[num])
                {
                    f=0;
                    break ;
                }
                int indx=0;
                ll pmvl=allprim[indx];
                while(pmvl*pmvl<=num)
                {
                    if(num%pmvl==0)
                    {
                        ans.pb(pmvl);
                        break ;
                    }
                    indx++;
                    if(indx==allprim.size())break;
                    pmvl=allprim[indx];
                }

            }
            if(f&&j&&ans.size()==9)
            {   bitset<16> nada(k);
                cout<<nada<<" ";
                fcout(9,ans);
                cout<<endl;j--;
            }




        }
    }


}
