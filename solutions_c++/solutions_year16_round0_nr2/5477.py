#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ll long long
#define debug(x) cout<<">value ("<<#x<<") : "<<x<<endl;
#define fr(i,beg,end) for(i=beg;i<end;i++)
#define itfr(it,stl) for(it=stl.begin();it!=stl.end();it++)
#define PII pair<int,int>
#define init(x,val) memset(x,val,sizeof(x))
#define fst first
#define snd second
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,t,T;
    string s;
    cin>>T;
    fr(t,1,T+1)
    {
        cin>>s;
        int p_prev=0;
        int n_prev=0;
        int p_new=0;
        int n_new=0;
        fr(i,0,s.length())
        {
            if(s[i]=='+')
            {
                p_new=p_prev;
                n_new=p_prev+1;
                p_prev=p_new;
                n_prev=n_new;
            }
            else
            {
                p_new=n_prev+1;
                n_new=n_prev;
                p_prev=p_new;
                n_prev=n_new;
            }
        }
        cout<<"Case #"<<t<<": "<<p_new<<endl;
    }
    return 0;
}
