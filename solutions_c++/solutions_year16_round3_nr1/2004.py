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
    freopen("A3.in","r",stdin);
    freopen("AO.out","w",stdout);
    int t,cs=1;
    cin>>t;
    int f[200];
    while(t--)
    {
        vector<char> v,vt;

        int n;
        cin>>n;
        for(int i=0; i<100; i++)
        {
            f[i]=0;
        }
        fora(i,n)
        {
            int x;
            cin>>x;
            f[i]=x;
        }
        int idx=-1,sum=0;
        while(1)
        {
            //cout<<"This";
            int mx=-1;
            sum=0;
            for(int i=0; i<26; i++)
            {
                sum+=f[i];
                if(f[i]>mx)
                {
                    mx=f[i];
                    idx=i;
                }
            }
            if(sum==0)
                break;
            if(sum==2 && mx==1)
            {
                for(int i=0; i<26; i++)
                {
                    if(f[i]==1)
                    {
                        vt.pub(char('A'+i));
                        f[i]--;
                    }
                }
            }
            else{
            //cout<<char('A'+idx)<<endl;
            v.pub(char('A'+idx));
            f[idx]--;
            }

        }
        cout<<"Case #"<<cs<<":";
        for(int i=0; i<v.size(); i++)
        {
            if(i%2==0)
            {
                cout<<" ";
            }
            cout<<v[i];

        }
        cout<<" ";cout<<vt[0]<<vt[1];
        cout<<endl;
        cs++;

    }
    return 0;
}
