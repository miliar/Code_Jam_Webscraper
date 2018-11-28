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
//freopen("ip.cpp","r",stdin);
freopen("B-large.in","r",stdin);
    freopen("OUTPUT.txt","w",stdout);

    char g;
    int t;
    cin>>t;
    char s[400];
    int cs=1;
    while(t--)
    {
        cin>>s;
        int ans=0;
        int len=strlen(s);
        while(1)
        {

            g=s[0];
            int ct=0;
            for(int i=0; i<len; i++)
            {
                if(s[i]==g)
                {
                    ct++;
                }
                else
                {
                    break;
                }
            }
            if(ct==len && g=='+')
            {
                break;
            }
            else
            {
                g=s[0];
                for(int i=0; i<len; i++)
                {
                    if(s[i]==g)
                    {
                        if(s[i]=='+')
                            s[i]='-';
                        else
                        s[i]='+';
                    }
                    else
                    {
                        break;
                    }
                }

            }
            ans++;

        }
        cout<<"Case #"<<cs<<": "<<ans<<endl;
        cs++;
    }
    return 0;
}
