#include<bits/stdc++.h>
//Definitions
#define LL long long
#define LLU unsigned long long
#define fora(var,end) for(int var=0;var<end;var++)
#define fore(var,start,end) for(int var=start;var<end;var++)
#define forit(it1,a) for(typeof(a.begin()) it1=a.begin();it1!=a.end();it1++)
#define pub push_back
#define fst first
#define snd second
#define MOD 1000000007
#define mkp make_pair
#define beg begin
#define ed end
#define pii pair<int,int>
#define all(v) v.begin(),v.end()
#define P(a,b) cout<<a<<" "<<b<<" "
#define PNL printf("\n")
#define vi vector<int>
#define vpi vector<pair<pair<int,int>,int> >
#define FL(a,n,x) fill(a,a+n,x)
#define db1(a) cout<<#a<<":"<<a<<endl;
#define db2(a,b) cout<<#a<<":"<<a<<" , "<<#b<<" : "<<b<<endl;
#define db3(a,b,c) cout<<#a<<":"<<a<<" , "<<#b<<":"<<b<<" , "<<#c<<":"<<c<<endl;
//AP_HAWKDOWN from hereon
using namespace std;
int main()
{
freopen("D-small-attempt0.in","r",stdin);
    freopen("OUTPUT.txt","w",stdout);
//freopen("ip.cpp","r",stdin);
int t,cs=1;
cin>>t;
LL k,c,s;
LL pw[100];
while(t--)
{
    cin>>k>>c>>s;
    pw[0]=1;
    for(int i=1;i<=c;i++)
    {
        pw[i]=pw[i-1]*k;
    }
    cout<<"Case #"<<cs<<": ";
    for(LL i=1;i<=k;i++)
    {
        cout<<i*pw[c-1]<<" ";
    }
    cout<<endl;
    cs++;

}
return 0;
}
