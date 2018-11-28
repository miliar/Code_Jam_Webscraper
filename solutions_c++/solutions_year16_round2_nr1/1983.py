/*input

*/

//Template

//Header files
#include <bits/stdc++.h>

//Shortcuts
#define lli long long int
#define fo(i,n) for(i=0;i<n;i++)
#define fi(i,a,n) for(i=a;i<=n;i++)
#define fd(i,n,a) for(i=n;i>=a;i--)
#define modulo 1000000007
#define gi(a) scanf("%d",&a)
#define gs(a) scanf("%s",a)
#define gll(a) scanf("%lld",&a)
#define glf(a) scanf("%lf",&a)
#define gui(a) scanf("%u",&a)
#define f(n) for(i=0;i<n;i++)
#define pn printf("\n")
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define min(a,b) (a<b)?a:b
#define max(a,b) (a>b)?a:b

using namespace std;

int main()
{
	freopen ("A-large.in","r",stdin);
    freopen ("out.txt","w",stdout);

    int t,tt,i,left;
    string s;
    gi(t);
    for(tt=1;tt<=t;tt++)
    {
        int arr[26];
        vector<int> vec;
        for(i=0;i<26;i++)
            arr[i]=0;
        cin>>s;
        for(i=0;i<s.length();i++)
        {
            arr[s[i]-'A']++;
        }
        left=s.length();
        while(left>0)
        {
            if(arr['Z'-'A']>0)
            {
                arr['Z'-'A']--;
                arr['E'-'A']--;
                arr['R'-'A']--;
                arr['O'-'A']--;
                left-=4;
                vec.pb(0);
            }
            else if(arr['W'-'A']>0)
            {
                arr['T'-'A']--;
                arr['W'-'A']--;
                arr['O'-'A']--;
                left-=3;
                vec.pb(2);
            }
            else if(arr['G'-'A']>0)
            {
                arr['E'-'A']--;
                arr['I'-'A']--;
                arr['G'-'A']--;
                arr['H'-'A']--;
                arr['T'-'A']--;
                left-=5;
                vec.pb(8);
            }
            else if(arr['X'-'A']>0)
            {
                arr['S'-'A']--;
                arr['I'-'A']--;
                arr['X'-'A']--;
                left-=3;
                vec.pb(6);
            }
            else if(arr['U'-'A']>0)
            {
                arr['F'-'A']--;
                arr['O'-'A']--;
                arr['U'-'A']--;
                arr['R'-'A']--;
                left-=4;
                vec.pb(4);
            }
            else if(arr['S'-'A']>0)
            {
                arr['S'-'A']--;
                arr['E'-'A']--;
                arr['V'-'A']--;
                arr['E'-'A']--;
                arr['N'-'A']--;
                left-=5;
                vec.pb(7);
            }
            else if(arr['V'-'A']>0)
            {
                arr['F'-'A']--;
                arr['I'-'A']--;
                arr['V'-'A']--;
                arr['E'-'A']--;
                left-=4;
                vec.pb(5);
            }
            else if(arr['T'-'A']>0)
            {
                arr['T'-'A']--;
                arr['H'-'A']--;
                arr['R'-'A']--;
                arr['E'-'A']--;
                arr['E'-'A']--;
                left-=5;
                vec.pb(3);
            }
            else if(arr['O'-'A']>0)
            {
                arr['O'-'A']--;
                arr['N'-'A']--;
                arr['E'-'A']--;
                left-=3;
                vec.pb(1);
            }
            else if(arr['N'-'A']>0)
            {
                arr['N'-'A']--;
                arr['I'-'A']--;
                arr['N'-'A']--;
                arr['E'-'A']--;
                left-=4;
                vec.pb(9);
            }
        }
        sort(vec.begin(),vec.end());
        printf("Case #%d: ",tt);
        for(i=0;i<vec.size();i++)
        {
            printf("%d",vec[i]);
        }
        printf("\n");
    }

    return 0;
}
