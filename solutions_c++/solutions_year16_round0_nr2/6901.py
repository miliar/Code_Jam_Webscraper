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
        int i,p;
        char s[105];
        cin>>s;
        int l= strlen(s);
        p=-1;
        //cout<<s<<" ";
        for(i=l-1;i>=0;i--)
        {
            if(s[i]=='+')
                continue;
            else
            {
                p=i;
                break;
            }
        }
        //cout<<p<<" ";
        l=p;
        int cnt=0;
        if(l==-1)
            cnt=0;
        else
            {
                for(i=1;i<=l;i++)
                {
                    if(s[i]==s[i-1])
                        continue;
                    else
                        cnt++;
                }
                cnt++;
            }
        cout<<cnt;nl;


    }
}
