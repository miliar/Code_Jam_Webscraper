/*********************
****SHASHANK GUPTA****
***@(my_blue_luck)****
**********************/

#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef long long int ll;

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

int main()
{
    ll t,x,cnt,i,l;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin >> t ;
    for(x=1;x<=t;x++)
    {
        char str[105],a;
        cin >> str ;
        l=strlen(str);
        cnt=0;
        if(str[0]=='+')
        {
            a='-';
            for(i=0;i<l;i++)
            {
                if(str[i]==a)
                {
                    cnt++;
                    if(a=='-')
                        a='+';
                    else
                        a='-';
                }
            }
            if(str[l-1]=='-')
                cout << "Case #" << x << ": " << cnt+1 << endl ;
            else
                cout << "Case #" << x << ": " << cnt << endl ;
        }
        else
        {
            a='+';
            for(i=0;i<l;i++)
            {
                if(str[i]==a)
                {
                    cnt++;
                    if(a=='+')
                        a='-';
                    else
                        a='+';
                }
            }
            if(str[l-1]=='+')
                cout << "Case #" << x << ": " << cnt << endl ;
            else
                cout << "Case #" << x << ": " << cnt+1 << endl ;
        }

    }
    return 0;
}
