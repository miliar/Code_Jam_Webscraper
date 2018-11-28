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
            int a[2550];
            memset(a,0,sizeof(a));
            int n,vl,i,j;
            cin>>n;
            for(i=1;i<=(2*n-1);i++)
            {
                for(j=1;j<=n;j++)
                {
                    cin>>vl;
                    a[vl]++;
                }

            }
       // for(i=1;i<=10;i++)
         //   printf("%d->%d\n",i,a[i]);
        vector<int>v;
        for(i=1;i<=2500;i++)
        {
            if(a[i]%2==1 and a[i]!=0)
                v.pb(i);
        }
        sort(v.begin(),v.end());
        for(i=0;i<v.size();i++)
            cout<<v[i]<<' ';
        nl;

    }
}
