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
    int t,tt,x,r,c;

    gi(t);
    for(tt=1;tt<=t;tt++){
        gi(x);
        gi(r);
        gi(c);

        if(x==1)
            printf("Case #%d: GABRIEL\n",tt);

        else if(x==4){
            if( (r==4 && c==4) || (r==3 && c==4) || (r==4 && c==3) ) {
                printf("Case #%d: GABRIEL\n",tt);
            }
            else
                printf("Case #%d: RICHARD\n",tt);
        }

        else if(x==2){
            if((r==1 && c==1) || (r==1 && c==3) || (r==3 && c==1) || (r==3 && c==3)){
                printf("Case #%d: RICHARD\n",tt);
            }
            else
                printf("Case #%d: GABRIEL\n",tt);
        }
        else if(x==3){
            if((r==2 && c==3) || (r==3 && c==2) || (r==3 && c==4) || (r==4 && c==3) ||(r==3 && c==3)){
                printf("Case #%d: GABRIEL\n",tt);
            }
            else
                printf("Case #%d: RICHARD\n",tt);
        }
    }

    return 0;
}

