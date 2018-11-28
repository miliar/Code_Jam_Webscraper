#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <sstream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <set>
#include <map>
#include <queue> 

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define pb push_back
#define mp make_pair
#define sz size()
#define ln length()
#define forr(i,a,b)                 for(int i=a;i<b;i++)
#define rep(i,n)                    forr(i,0,n) 
#define all(v)                      v.begin(),v.end()    
#define uniq(v)                     sort(all(v));v.erase(unique(all(v)),v.end())
#define clr(a)                      memset(a,0,sizeof a)
    
#define debug                       if(1)
#define debugoff                    if(0)    

#define print(x)                 cerr << x << " ";    
#define pn()                     cerr << endl;
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;

#define MAX 100010
#define MOD 1000000007
int main()
{
    int cases=0,tc,n;
    double C,F,X,R,total,ta,tb,t;
    scanf("%d",&tc);
    while(tc--)
    {
        cases++;
        scanf("%lf %lf %lf",&C,&F,&X);
        R = 2;
        total = 0;
        while(1)
        {
            tb = total + (X/R);
            t = C/R;
            R += F;
            total += t;
            ta = total + (X/R);
            if(tb < ta) 
                break;
        }
        printf("Case #%d: %.7lf\n",cases,tb);
    }
    return 0; 
}
