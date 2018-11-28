#include<bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define y0 hi1
#define y1 hi2
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(a) (a)*(a)
#define ld long double
#define all(a) (a).begin(), (a).end()

using namespace std;

main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    int num=0;
    while(T--)
    {
        num++;
        int k;
        cin>>k;
        k++;
        char a[k];
        string S;
        cin>>S;
        for(int i=0; i<k; i++)
            a[i]=(S[i]-'0');
        int s=a[0];
        int ans=0;
        for(int i=1; i<k; i++)
        {
            if(s<i)
            {
                ans+=i-s;
                s=i;
            }
            s+=a[i];
        }
        cout<<"Case #"<<num<<": "<<ans<<"\n";
    }
}
