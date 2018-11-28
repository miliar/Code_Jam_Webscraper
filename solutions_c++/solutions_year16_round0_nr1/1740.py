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
LL  ans[2010000];
int d[11];
int main()
{
int ma=0;
//freopen("ip.cpp","r",stdin);
//A-small-attempt0

freopen("A-large.in","r",stdin);
    //freopen("OUTPUT.txt","w",stdout);
int t;
for(LL i=1;i<=1000001;i++)
{
    for(int k=0;k<=9;k++)
    {
        d[k]=0;
    }
    int ct=0;
    for(LL j=1;;j++)
    {

        LL temp=i*j;
        LL tempx=temp;
        ma=max(j,(LL)ma);
        while(temp>0)
        {
            if(d[temp%10]==0)
            {
                ct++;
                d[temp%10]=1;
            }
            if(ct==10)
            {
                ans[i]=tempx;
                break;

            }
            temp/=10;
        }
        if(ct==10)
        {
            break;
        }
    }
}
cin>>t;
int s;
int cs=1;
while(t--)
{
    cin>>s;
    cout<<s<<endl;
    if(s==0)
    {
        cout<<"Case #"<<cs<<": INSOMNIA"<<endl;
    }
    else
    {
        cout<<"Case #"<<cs<<": "<<ans[s]<<endl;
    }
    cs++;
}

return 0;
}
