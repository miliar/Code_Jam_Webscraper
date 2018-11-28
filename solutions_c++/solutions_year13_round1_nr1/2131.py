#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#define pi 3.14159
using namespace std;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t,i=1,j;
    long long c,r,b,d;
    scanf("%d",&t);
    while(t!=0) {
        scanf("%lld %lld",&r,&b);
        c=0;
        d=0;
        for(j=0; j<b; j=j+2) {
            c=c+(((r+j+1)*(r+j+1)-(r+j)*(r+j)));
            if(c>b)
                break;
            else
                d++;
        }
        cout<<"Case #"<<i<<":"<<" "<<d<<"\n";
        t--;
        i++;
    }
    return 0;
}
