#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<cstdlib>
#include<sstream>
#include<string.h>
#include<set>
#include<map>
#include<assert.h>
#include<ctime>
#include<queue>
#include<vector>
#include<stack>
#include<list>
#include<math.h>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef long long int lli;

#define MAXN 1000005
#define INF 2147483647
#define MOD 1000000007
#define pb push_back 
#define sz(a) int((a).size())
#define FOR(x,a,b) for(int (x) = (a);(x)<=(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define all(c) c.begin(),c.end()
#define mset(a,b) memset(a,b,sizeof(a))



int main()
{
    int t;
    long double c,f,x,steps,speed;
    int cc = 0;
    
    // #ifndef ONLINE_JUDGE
    // freopen("input.txt","r",stdin);
    // #endif

    scanf("%d",&t);
    rep(q,t)
    {
        cc = 0;
        steps=0.0;
        speed=2.0;
        scanf("%Lf%Lf%Lf",&c,&f,&x);
        if(x<c)
        {
            steps=x/speed;
        }
        else
        {
            while(true)
            {
                if((x/speed)<((c/speed)+(x/(speed+f))))
                {
                    steps=steps+(x/speed);
                    break;
                }
              //  cc++;
                steps=steps+c/speed;
                speed=speed+f;
                
            }
       }
         printf("Case #%d: %0.7Lf\n",q+1,steps);   
        
    }


    return 0;
}