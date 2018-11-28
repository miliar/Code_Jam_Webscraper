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
    long testCase,x,y,a,b,k;
    cin>>testCase;
    for(int qq=1;qq<=testCase;qq++)
    {
        cin>>a>>b>>k;
        int ways=0;
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                if((i&j)<k)
                    {
                        //cout<<i<<" "<<b<<endl;
                        ways++;
                    }
            }
        }
        printf("Case #%d: %d\n", qq,ways);
    }
    return 0;
}




