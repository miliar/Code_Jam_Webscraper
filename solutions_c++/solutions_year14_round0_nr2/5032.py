#include<iostream>
#include<cstdio>
#include<cmath>
#include<sstream>
#include<ctime>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<map>
#include<set>
#define mp make_pair
#define pb push_back
#define max(a,b)a>b?a:b
#define min(a,b)a<b?a:b
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

int main ()
{
    //freopen("out.txt","w",stdout);
    //freopen("in.txt","r",stdin);
    int testCase;
    double rate,x,y,c,f;
    cin>>testCase;
    for(int qq=1;qq<=testCase;qq++)
    {
        cin>>c>>f>>x;
        rate=2;
        double time=0;
        while(2)
        {
            time+=c*1.0/rate;
            double now,factory;
            now=(x-c)*1.0/rate;
            factory=x*1.0/(rate+f);
            if(factory<now)
                rate+=f;
            else
            {
                time+=(x-c)*1.0/rate;
                break;
            }
            
        }
        printf("Case #%d: ", qq);
        //cout<<time;
        printf("%.7lf\n", time);
        
    }
    return 0;
}




