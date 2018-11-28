#include<bits/stdc++.h>
#define MOD 1000000007
#define len(a) strlen(a)
#define ll long long
#define nl printf("\n")
#define F first
#define S second
#define db printf("debug")
#define yes printf("YES\n")
#define no printf("NO\n")
#define pb(a) push_back(a)
#define po(a) pop_back()
#define mp(a,b) make_pair(a,b)
#define set(a,v) memset(a,v,sizeof(a))
#define sz(v) v.size()
#define gc getchar//_unlocked
#define pcase(i) printf("Case #%d: ",i)

using namespace std;


int main()
{
    int t;
    scanf("%d",&t);
    for(int x=1;x<=t;x++)
    {
        pcase(x);
        int i=0;
        string ans,s,tmp,tmp2;
        cin>>s;
        ans=s[0];
        int l= s.length();
        for(i=1;i<l;i++)
        {
            tmp=s[i]+ans;
            tmp2= ans+s[i];
            if(tmp2>tmp)
                ans=tmp2;
            else
                ans= tmp;
        }
        cout<<ans;nl;




    }
}
