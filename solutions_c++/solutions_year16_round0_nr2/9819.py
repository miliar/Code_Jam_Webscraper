//Bismillahir Rahmanir Rahim
//Opu-1204026
#include<bits/stdc++.h>
using namespace std;
#define sf      scanf
#define pf      printf
#define pb      push_back
#define _       ios_base::sync_with_stdio(false);
#define ct      cin.tie(NULL);
#define ll      long long
#define eps     1e-10
#define ms(n,i) memset(n,i,sizeof n)
#define pi      2*acos(0)
#define inf     1<<30
#define fr(i,n) for(i=0;i<n;i++)
#define fr1(i,n)for(i=1;i<=n;i++)
#define nl cout<<"\n"
#define abs(x)  ((x<0)?-(x):x)
#define MAX 30005
#define sp(i)      cout<<fixed<<setprecision(i)
//STL
typedef      vector<int> vi;
typedef      vector<ll> vl;
typedef      pair<int,int>ii;
typedef      vector<ii> vii;
#define mp      make_pair
#define ft      first
#define sd      second
#define IT      iterator
#define pr(c,x) ((c).find(x)!=(c).end())
#define sz(a) int((a).size())
#define all(c)  c.begin(), c.end()
#define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=c.end();i++)
#define vpresent(c,x) (find(all(c),x)!=(c).end())


string flip(string s,int i,int j)
{
    int n,k;
    n=s.length();
    string s1="";
    for(k=j+1; k<n; k++)
        s1+=s[k];
    while(i<=j)
    {
        if(s[i]=='+')
            s1='-'+s1;
        else
            s1='+'+s1;
        i++;
    }
    return s1;
}

int main()
{
   // freopen("F:\\Coding\\in.txt","r",stdin);
   // freopen("F:\\Coding\\out.txt","w",stdout);
    _;ct;
    int t,z,i,j,n,k,cn;
    string s;
    cin>>t;
    fr1(z,t)
    {
        cin>>s;
        n=s.length();
        k=n-1;
//        while(k>=0)
//        {
//            if(s[k]=='-')break;
//            k--;
//        }
        cn=0;
        i=0;
        while(1)
        {
            // cout<<s<<endl;
            while(k>=0)
            {
                if(s[k]=='-')break;
                k--;
            }
            if(k<0)break;
            if(s[i]=='-')
            {
                s=flip(s,i,k);
            }
            else
            {
                for(j=i; j<k; j++)
                {
                    if(s[j+1]=='-')break;
                }
                s=flip(s,i,j);
            }
            cn++;

        }
        cout<<"Case #"<<z<<": "<<cn;nl;
    }

    return 0;
}

