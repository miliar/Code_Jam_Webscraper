//Template

//Header files
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <map>
#include <algorithm>
#include <stack>
#include <list>

//Shortcuts
#define lli long long int
#define fo(i,n) for(i=0;i<n;i++)
#define fi(i,a,n) for(i=a;i<=n;i++)
#define fd(i,n,a) for(i=n;i>=a;i--)
#define modulo 1000000007
#define gi(a) scanf("%d",&a)
#define f(n) for(i=0;i<n;i++)
#define pn printf("\n")
#define pb push_back

using namespace std;

int main()
{
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);

    int t,tt,i,smax,present,required;
    char s[1002];
    gi(t);
    fi(tt,1,t){
        present=0;
        required=0;
        gi(smax);
        scanf("%s",s);
        fo(i,smax+1){
            if(present<i){
                required+=(i-present);
                present+=(i-present);
            }
            present+=(s[i]-48);
        }
        printf("Case #%d: %d\n",tt,required);
    }
    return 0;
}

